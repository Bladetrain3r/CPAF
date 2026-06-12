import numpy as np
np.random.seed(0)

print("="*70)
print("CLAIM 1: S_ij = |exp(i(theta_j - theta_i))| as a synchrony measure")
print("Doc claims: =1 at dtheta=0, =0 at dtheta=pi, smooth gradient between")
print("="*70)
for d in [0, np.pi/4, np.pi/2, 3*np.pi/4, np.pi, 1.234, -2.0]:
    s = np.abs(np.exp(1j*d))
    print(f"  dtheta={d:+.3f} rad -> |exp(i*dtheta)| = {s:.6f}")
print(">> |exp(i*real)| is the modulus of a UNIT phasor: identically 1.")
print(">> The claimed gradient (0 at pi) is FALSE. Measure is constant 1.\n")

print("="*70)
print("CLAIM 1b: Candidate intended measures vs the doc's stated properties")
print("="*70)
print(f"{'dtheta':>8} | {'cos(d)':>8} | {'(1+cos)/2':>10} | {'|cos(d/2)|=orderparam':>20}")
for d in [0, np.pi/4, np.pi/2, 3*np.pi/4, np.pi]:
    cosd = np.cos(d)
    half = (1+np.cos(d))/2
    op = np.abs((np.exp(1j*0)+np.exp(1j*d))/2)  # local order param of 2 oscillators
    print(f"{d:8.3f} | {cosd:8.3f} | {half:10.3f} | {op:20.6f}")
print(">> |(e^{i*th_i}+e^{i*th_j})/2| = |cos(dtheta/2)| matches stated props")
print("   (1 at 0, 0 at pi, smooth). cos(dtheta) matches the SIGNED STDP story.")
print("   The doc conflates these two different targets.\n")

print("="*70)
print("CLAIM 2: Consequence for the Hebbian update if S==1 (as written)")
print("  dK_ij = eta*(S*R) - lambda*K  with S==1 -> dK = eta*R - lambda*K")
print("  -> identical for ALL pairs; no dependence on phase relationship.")
print("="*70)

def coupling_from_kohonen(N):
    # toy spatial coupling: nodes on a line, gaussian of distance
    pos = np.arange(N)
    D = np.abs(pos[:,None]-pos[None,:])
    K = np.exp(-(D**2)/2.0)
    np.fill_diagonal(K,0)
    return K

def run(measure, blend=True, steps=2000, N=8, dt=0.01, eta=0.01, lam=0.001):
    omega = np.random.randn(N)*0.5
    theta = np.random.rand(N)*2*np.pi
    Ksp = coupling_from_kohonen(N)
    K = Ksp + np.random.randn(N,N)*0.1
    K = (K+K.T)/2
    np.fill_diagonal(K,0)
    for t in range(steps):
        # reward: global order parameter minus baseline
        r = np.abs(np.mean(np.exp(1j*theta)))
        R = r - 0.5
        dtheta = omega.copy()
        diff = theta[None,:]-theta[:,None]  # theta_j - theta_i
        dtheta += (K*np.sin(diff)).sum(axis=1)/N
        theta = theta + dtheta*dt
        d = theta[None,:]-theta[:,None]
        if measure=='asis':
            S = np.abs(np.exp(1j*d))
        elif measure=='cos':
            S = np.cos(d)
        elif measure=='order':
            S = np.abs(0.5*(np.exp(1j*theta)[:,None]+np.exp(1j*theta)[None,:]))
        np.fill_diagonal(S,0)
        dK = eta*(S*R) - lam*K
        K = np.maximum(K + dK*dt, 0)
        if blend:
            K = 0.8*K + 0.2*Ksp
    return K, Ksp

for meas in ['asis','cos','order']:
    K,Ksp = run(meas, blend=True)
    # how much does learned K deviate from spatial, and does it vary by pair?
    dev = np.linalg.norm(K-Ksp)/np.linalg.norm(Ksp)
    print(f"  measure={meas:6s} blend=ON : ||K-Ksp||/||Ksp|| = {dev:.4f}")
print("  -> with blend ON every step, K stays pinned near Ksp regardless.\n")

for meas in ['asis','cos','order']:
    K,Ksp = run(meas, blend=False)
    dev = np.linalg.norm(K-Ksp)/np.linalg.norm(Ksp)
    # variance of off-diagonal coupling = does structure differentiate?
    off = K[~np.eye(K.shape[0],dtype=bool)]
    print(f"  measure={meas:6s} blend=OFF: dev={dev:.3f}  K range=[{off.min():.3f},{off.max():.3f}] std={off.std():.3f}")
print("  -> 'asis' (S==1) gives uniform drive; 'cos'/'order' differentiate by phase.\n")

print("="*70)
print("CLAIM 3: blend step strength.  K <- 0.8*K + 0.2*Ksp applied per step,")
print("  NOT scaled by dt. Compare to Hebbian decay lambda*dt per step.")
print("="*70)
dt,lam=0.01,0.001
print(f"  spatial pull per step      = 0.2")
print(f"  Hebbian decay per step     = lambda*dt = {lam*dt}")
print(f"  ratio                      = {0.2/(lam*dt):.0f}x stronger\n")

print("="*70)
print("CLAIM 4: Connectivity entropy H(K) = -sum K_ij log K_ij")
print("  K_ij not normalized, can exceed 1, undefined at K=0 (the clamp floor)")
print("="*70)
K = np.array([0.0, 0.5, 1.0, 2.0])
with np.errstate(divide='ignore', invalid='ignore'):
    terms = -K*np.log(K)
print(f"  K values:          {K}")
print(f"  -K*log(K) terms:   {terms}  (note nan at K=0, negative at K>1)")
print(f"  sum (naive)        = {np.nansum(terms):.4f}  -> not a valid entropy")
ptot = K.sum()
p = K/ptot
with np.errstate(divide='ignore', invalid='ignore'):
    Hnorm = -np.nansum(np.where(p>0, p*np.log(p), 0))
print(f"  normalized entropy = {Hnorm:.4f}  (proper form needs p=K/sum(K))")
