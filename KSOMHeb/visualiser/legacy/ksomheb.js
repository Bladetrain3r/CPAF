/*
 * K-SOM-Heb dynamics -- JavaScript port of ksomheb.py (v1.1, Hebbian path).
 *
 * This is the SAME math as the verified Python reference. It is exercised two
 * ways from one source: the browser visualiser loads it as a <script>, and
 * parity_check.js runs it under Node to confirm it reproduces Python's numbers
 * (see that file). Keep this file the single source for the JS side -- do not
 * inline a second copy in the HTML.
 *
 * Matrices are stored as flat Float64Array of length N*N, row-major:
 *   K[i*N + j] is the influence of oscillator j on oscillator i.
 */
(function (root) {
  "use strict";

  // Global Kuramoto order parameter. Returns {r, psi}:
  //   z = (1/N) sum_j exp(i*theta_j) = r * exp(i*psi)
  function orderParameter(theta) {
    let cx = 0, cy = 0, N = theta.length;
    for (let j = 0; j < N; j++) { cx += Math.cos(theta[j]); cy += Math.sin(theta[j]); }
    cx /= N; cy /= N;
    return { r: Math.hypot(cx, cy), psi: Math.atan2(cy, cx) };
  }

  // Pairwise synchrony S[i*N+j] = |cos((theta_j - theta_i)/2)|, diagonal 0.
  function localSynchrony(theta, out) {
    const N = theta.length;
    const S = out || new Float64Array(N * N);
    for (let i = 0; i < N; i++) {
      for (let j = 0; j < N; j++) {
        S[i * N + j] = (i === j) ? 0 : Math.abs(Math.cos((theta[j] - theta[i]) / 2));
      }
    }
    return S;
  }

  // dtheta_i = omega_i + (1/N) sum_j K_ij sin(theta_j - theta_i)
  function kuramotoStep(theta, omega, K, dt, outTheta) {
    const N = theta.length;
    const tn = outTheta || new Float64Array(N);
    for (let i = 0; i < N; i++) {
      let acc = 0;
      const ti = theta[i], base = i * N;
      for (let j = 0; j < N; j++) acc += K[base + j] * Math.sin(theta[j] - ti);
      tn[i] = ti + (omega[i] + acc / N) * dt;
    }
    return tn;
  }

  // One step of phases AND Hebbian coupling.
  //   dK_ij/dt = eta * S_ij * R - lam * K_ij,   clipped to [0, K_max]
  // Mutates K in place; returns the new theta array.
  function updateStep(theta, omega, K, reward, p, scratch) {
    const N = theta.length;
    const dt = p.dt, eta = p.eta, lam = p.lam, Kmax = p.K_max;
    const tn = kuramotoStep(theta, omega, K, dt, scratch.theta);
    const S = localSynchrony(tn, scratch.S);
    for (let k = 0; k < N * N; k++) {
      const dK = eta * (S[k] * reward) - lam * K[k];
      let v = K[k] + dK * dt;
      if (v < 0) v = 0; else if (v > Kmax) v = Kmax;
      K[k] = v;
    }
    return tn;
  }

  // Shannon entropy of the normalized coupling distribution (excludes diagonal).
  function connectivityEntropy(K, N) {
    let total = 0;
    for (let i = 0; i < N; i++)
      for (let j = 0; j < N; j++) if (i !== j) total += K[i * N + j];
    if (total <= 0) return 0;
    let H = 0;
    for (let i = 0; i < N; i++)
      for (let j = 0; j < N; j++) {
        if (i === j) continue;
        const pij = K[i * N + j] / total;
        if (pij > 0) H -= pij * Math.log(pij);
      }
    return H;
  }

  const api = { orderParameter, localSynchrony, kuramotoStep, updateStep, connectivityEntropy };
  if (typeof module !== "undefined" && module.exports) module.exports = api;
  root.KSOMHeb = api;
})(typeof window !== "undefined" ? window : globalThis);
