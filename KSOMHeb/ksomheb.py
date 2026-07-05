"""
K-SOM-Heb reference implementation (v1.1, Hebbian path).

This module is the executable counterpart to KSOMHeb_Architecture.md. It is
built up and checked one claim at a time by the scripts in verification/.

Conventions
-----------
theta : (N,) array of oscillator phases, radians.
omega : (N,) array of natural frequencies, radians per unit time.
K     : (N, N) coupling matrix. K[i, j] is the influence of j on i.
        Symmetric and non-negative in the baseline (pure Hebbian) model.

The phase dynamics are the adaptive Kuramoto model:

    dtheta_i/dt = omega_i + (1/N) * sum_j K[i,j] * sin(theta_j - theta_i)

With a uniform all-to-all coupling K[i,j] = K this reduces to the classic
Kuramoto model with global coupling strength K, which is what iteration 1
checks against known theory.
"""
import numpy as np


def order_parameter(theta):
    """Global Kuramoto order parameter.

    Returns (r, psi) where the complex order parameter is
        z = (1/N) * sum_j exp(i * theta_j) = r * exp(i * psi)
    r in [0, 1] measures phase coherence: r = 1 is perfect synchrony,
    r ~ 0 is an incoherent (uniformly scattered) phase distribution.
    psi is the average phase (the direction the mean arrow points).
    """
    z = np.mean(np.exp(1j * np.asarray(theta)))
    return np.abs(z), np.angle(z)


def local_synchrony(theta):
    """Pairwise synchrony matrix S[i,j] = |cos((theta_j - theta_i) / 2)|.

    This is the magnitude of the two-oscillator order parameter,
    |(exp(i theta_i) + exp(i theta_j)) / 2|. It is 1 in phase, 0 anti-phase,
    smooth in between, and (being built from complex exponentials) immune to
    phase wrapping. The diagonal is set to 0 (no self-coupling).
    """
    theta = np.asarray(theta)
    d = theta[None, :] - theta[:, None]          # d[i,j] = theta_j - theta_i
    S = np.abs(np.cos(d / 2.0))
    np.fill_diagonal(S, 0.0)
    return S


def kuramoto_dtheta(theta, omega, K):
    """Right-hand side of the adaptive Kuramoto ODE (vectorized)."""
    theta = np.asarray(theta)
    N = theta.shape[0]
    d = theta[None, :] - theta[:, None]          # theta_j - theta_i
    return omega + (K * np.sin(d)).sum(axis=1) / N


def kuramoto_step(theta, omega, K, dt=0.01):
    """One explicit-Euler step of the phase dynamics (coupling fixed)."""
    return theta + kuramoto_dtheta(theta, omega, K) * dt


def update_ksom_heb(theta, omega, K, reward, dt=0.01,
                    eta=0.01, lam=0.001, K_max=2.0):
    """One step of phases AND Hebbian coupling.

    Coupling update is an Euler step of
        dK_ij/dt = eta * S_ij * R_ij - lam * K_ij
    bounded into [0, K_max]. Spatial structure (if any) belongs in the
    initial K, not re-applied here.

    ``reward`` may be:
      * a scalar  -> global reward R, shared by every pair (iterations 1-3);
      * a vector R_i of shape (N,) -> per-node reward, mapped to pairs
        symmetrically as R_ij = (R_i + R_j) / 2 (local/hybrid, iteration 4);
      * a full (N, N) matrix, used as-is.
    The scalar path is identical to the original rule, so the JS parity
    check is unaffected.
    """
    theta_new = kuramoto_step(theta, omega, K, dt)
    S = local_synchrony(theta_new)
    R = reward_matrix(reward)
    dK = eta * (S * R) - lam * K
    K_new = np.clip(K + dK * dt, 0.0, K_max)
    return theta_new, K_new


def reward_matrix(reward):
    """Broadcast a reward into a pairwise form for the coupling update.

    scalar -> scalar (broadcasts); (N,) vector -> (N,N) with (R_i+R_j)/2;
    (N,N) -> returned unchanged.
    """
    R = np.asarray(reward, dtype=float)
    if R.ndim == 0:
        return R
    if R.ndim == 1:
        return 0.5 * (R[:, None] + R[None, :])
    return R


def local_field_coherence(theta, K, eps=1e-12):
    """Per-node local order parameter r_local[i] in [0, 1] (endogenous).

    r_local[i] = |sum_j K_ij exp(i theta_j)| / sum_j K_ij

    The magnitude of the coupling-weighted mean field that node i actually
    feels: high when the neighbours i is coupled to point the same way, low
    when they disagree. Uses only theta and K -- no ground-truth labels -- so
    it is a legitimate local reward signal. Nodes with no coupling get 0.
    """
    theta = np.asarray(theta)
    K = np.asarray(K, dtype=float)
    deg = K.sum(axis=1)
    field = (K * np.exp(1j * theta)[None, :]).sum(axis=1)
    return np.where(deg > eps, np.abs(field) / (deg + eps), 0.0)


def modularity(K, groups):
    """Weighted Newman modularity Q of coupling matrix K for a given partition.

    Q = (1/2m) sum_ij [A_ij - k_i k_j / 2m] * delta(g_i, g_j),
    with A = K (diagonal zeroed), k_i = sum_j A_ij, 2m = sum_ij A_ij.
    Q > 0 means more within-group weight than expected by chance.
    """
    A = np.array(K, dtype=float)
    np.fill_diagonal(A, 0.0)
    m2 = A.sum()
    if m2 == 0:
        return 0.0
    k = A.sum(axis=1)
    groups = np.asarray(groups)
    same = groups[:, None] == groups[None, :]
    return float(((A - np.outer(k, k) / m2) * same).sum() / m2)


def connectivity_entropy(K):
    """Shannon entropy of the normalized coupling distribution.

    p_ij = K_ij / sum(K); H = -sum p_ij log p_ij, with 0*log0 := 0.
    Returns 0 for an all-zero matrix.
    """
    K = np.asarray(K, dtype=float)
    total = K.sum()
    if total <= 0:
        return 0.0
    p = (K / total).ravel()
    p = p[p > 0]
    return float(-(p * np.log(p)).sum())
