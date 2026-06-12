/*
 * Parity check: confirm ksomheb.js (the visualiser's math) reproduces the
 * verified Python reference (ksomheb.py) to floating-point tolerance.
 *
 * Reference values were produced by ksomheb.py for a fixed N=5 input
 * (see KSOMHeb/visualiser/README.md). Run:  node parity_check.js
 */
const K = require("./ksomheb.js");

const N = 5;
const theta = [0.0, 0.5, 1.1, 2.3, 3.0];
const omega = [0.1, -0.2, 0.05, 0.0, -0.15];
const Kmat = [
  0.0, 0.4, 0.3, 0.2, 0.1,
  0.4, 0.0, 0.5, 0.1, 0.2,
  0.3, 0.5, 0.0, 0.6, 0.3,
  0.2, 0.1, 0.6, 0.0, 0.4,
  0.1, 0.2, 0.3, 0.4, 0.0,
];
const R = 0.15;
const p = { dt: 0.05, eta: 0.01, lam: 0.001, K_max: 2.0 };

// Reference numbers from Python (ksomheb.py).
const ref = {
  r: 0.471238, psi: 1.280286,
  theta_new: [0.011224, 0.493076, 1.105434, 2.294519, 2.985746],
  K_new_0_1: 0.40005283,
  // a few synchrony entries: S[0,1], S[0,4], S[2,3]
  S_0_1: Math.abs(Math.cos((0.5 - 0.0) / 2)),
  S_0_4: Math.abs(Math.cos((3.0 - 0.0) / 2)),
};

let fails = 0;
function approx(name, got, want, tol = 1e-5) {
  const ok = Math.abs(got - want) <= tol;
  if (!ok) fails++;
  console.log(`  ${ok ? "PASS" : "FAIL"}  ${name}: got ${got.toFixed(6)}, want ${want.toFixed(6)}`);
}

const op = K.orderParameter(theta);
approx("order parameter r", op.r, ref.r);
approx("order parameter psi", op.psi, ref.psi);

const S = K.localSynchrony(theta);
approx("S[0,1]", S[0 * N + 1], ref.S_0_1);
approx("S[0,4]", S[0 * N + 4], ref.S_0_4);

const Kwork = Float64Array.from(Kmat);
const scratch = { theta: new Float64Array(N), S: new Float64Array(N * N) };
const tn = K.updateStep(theta, omega, Kwork, R, p, scratch);
for (let i = 0; i < N; i++) approx(`theta_new[${i}]`, tn[i], ref.theta_new[i]);
approx("K_new[0,1]", Kwork[0 * N + 1], ref.K_new_0_1, 1e-7);

console.log(fails === 0 ? "\nPARITY OK -- JS matches Python reference"
                        : `\n${fails} MISMATCH(ES)`);
process.exit(fails === 0 ? 0 : 1);
