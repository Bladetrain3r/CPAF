# Two-oscillator "entangle / disentangle" demo (Kuramoto-style coupling).
#
# PROVENANCE: an early exploratory script (Opus3/GPT3-era, via Ziggy), preserved
# here as the seed of iteration 6. It toggles the coupling on and off and plots
# the phases, phase difference, and N=2 order parameter R = |cos(dphi/2)|.
#
# NOTE: K_on = 3.0 is ~32x the locking threshold Kc = |w1-w2|/2 = 0.094, so this
# demo sits deep in the locked regime and shows locking ON vs OFF -- it does not
# probe the transition itself. iter6_locking_threshold.py sweeps K through Kc to
# make the bifurcation (and the 1/sqrt(2) coherence onset) rigorous. Kept as-is
# for reference; the analysis lives in iter6.

import numpy as np
import matplotlib.pyplot as plt

# Simulation params
dt = 0.002
T  = 20.0
t  = np.arange(0, T, dt)

# Natural frequencies (slightly detuned photons-as-oscillators surrogate)
w1 = 2.0 * np.pi * 1.00    # ~1 Hz
w2 = 2.0 * np.pi * 1.03    # ~1.03 Hz

# Coupling schedule: free (0-6s), entangle (6-14s), free (14-20s)
K_on = 3.0
def K_of_time(tt):
    if tt < 6.0:
        return 0.0
    elif tt < 14.0:
        return K_on
    else:
        return 0.0

# Small phase diffusion (optional) to show locking robustness
sigma = 0.03  # noise strength

# State arrays
phi1 = np.zeros_like(t)
phi2 = np.zeros_like(t)

# Random initial phases
phi1[0] = np.random.uniform(0, 2*np.pi)
phi2[0] = np.random.uniform(0, 2*np.pi)

# Integration (Euler-Maruyama)
for k in range(len(t)-1):
    Kt = K_of_time(t[k])
    # Kuramoto pair dynamics
    dphi1 = w1 + Kt * np.sin(phi2[k] - phi1[k])
    dphi2 = w2 + Kt * np.sin(phi1[k] - phi2[k])
    # Noise
    dphi1 += sigma * np.sqrt(dt) * np.random.randn()
    dphi2 += sigma * np.sqrt(dt) * np.random.randn()
    # Step
    phi1[k+1] = phi1[k] + dphi1 * dt
    phi2[k+1] = phi2[k] + dphi2 * dt

# Wrap to [0, 2pi)
phi1 = np.mod(phi1, 2*np.pi)
phi2 = np.mod(phi2, 2*np.pi)

# Phase difference and Kuramoto order parameter R
dphi = np.unwrap(phi1 - phi2)
# Order parameter for N=2: R = |(e^{i phi1} + e^{i phi2})/2|
R = np.abs(0.5 * (np.exp(1j*phi1) + np.exp(1j*phi2)))

# Coupling over time for reference
K_series = np.array([K_of_time(tt) for tt in t])

# Plot 1: phases vs time
plt.figure(figsize=(9, 4.8))
plt.plot(t, phi1, label="phi1(t)")
plt.plot(t, phi2, label="phi2(t)")
plt.plot(t, K_series*(2*np.pi/K_on), linestyle="--", label="K(t) scaled")
plt.title("Two-Oscillator Phases with Time-Varying Coupling")
plt.xlabel("Time (s)")
plt.ylabel("Phase (radians)")
plt.legend()
plt.tight_layout()
plt.show()

# Plot 2: phase difference & order parameter
plt.figure(figsize=(9, 4.8))
plt.plot(t, np.mod(dphi, 2*np.pi), label="Phase difference Δφ mod 2π")
plt.plot(t, R, label="Order parameter R (N=2)")
plt.plot(t, K_series/K_on, linestyle="--", label="K(t)/K_on")
plt.title("Locking (Δφ stabilizes) and Coherence (R rises) during Coupling")
plt.xlabel("Time (s)")
plt.ylabel("Value")
plt.legend()
plt.tight_layout()
plt.show()
