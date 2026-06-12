import numpy as np
np.random.seed(1)

# ---- exact corrected update function as written in the doc (v1.1) ----
def update_ksom_heb(theta, omega, K, reward, dt=0.01,
                    eta=0.01, lam=0.001, K_max=2.0):
    N = len(theta)
    dtheta = omega.copy()
    for i in range(N):
        for j in range(N):
            if i != j:
                dtheta[i] += (K[i, j] / N) * np.sin(theta[j] - theta[i])
    theta_new = theta + dtheta * dt
    S = np.zeros((N, N))
    for i in range(N):
        for j in range(N):
            if i != j:
                phase_diff = theta_new[j] - theta_new[i]
                S[i, j] = np.abs(np.cos(phase_diff / 2.0))
    dK = eta * (S * reward) - lam * K
    K_new = np.clip(K + dK * dt, 0.0, K_max)
    return theta_new, K_new

# ---- corrected connectivity entropy ----
def connectivity_entropy(K):
    Ksum = K.sum()
    if Ksum == 0:
        return 0.0
    p = (K / Ksum).ravel()
    p = p[p > 0]
    return float(-(p * np.log(p)).sum())

N = 8
pos = np.arange(N)
Ksp = np.exp(-(np.abs(pos[:,None]-pos[None,:])**2)/2.0); np.fill_diagonal(Ksp,0)
K = Ksp + np.random.randn(N,N)*0.1; K=(K+K.T)/2; np.fill_diagonal(K,0)
theta = np.random.rand(N)*2*np.pi
omega = np.random.randn(N)*0.5

P_trace=[]
K_prev=K.copy()
for t in range(5000):
    r = np.abs(np.mean(np.exp(1j*theta)))
    R = r - 0.5
    theta, K = update_ksom_heb(theta, omega, K, R)
    if t % 1000 == 0:
        P = np.linalg.norm(K-K_prev)/ (1.0)  # plasticity index proxy
        print(f"step {t:5d}: order r={r:.3f}  K[min,max]=[{K.min():.3f},{K.max():.3f}]  "
              f"H(K)={connectivity_entropy(K):.3f}  ||dK||={P:.4f}")
    K_prev=K.copy()

print()
print("Checks:")
print(f"  K bounded in [0, K_max=2.0]?           {K.min()>=0 and K.max()<=2.0}")
print(f"  K deviated from spatial baseline?       {np.linalg.norm(K-Ksp)/np.linalg.norm(Ksp):.3f} (was ~0.000 when frozen)")
print(f"  Synchrony S varies across pairs?")
d = theta[None,:]-theta[:,None]
S = np.abs(np.cos(d/2)); np.fill_diagonal(S,0)
off = S[~np.eye(N,dtype=bool)]
print(f"     S range=[{off.min():.3f},{off.max():.3f}] std={off.std():.3f}  (was identically 1.000)")
print(f"  Entropy H(K) finite & non-negative?     {np.isfinite(connectivity_entropy(K)) and connectivity_entropy(K)>=0}")
