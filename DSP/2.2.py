import numpy as np
import matplotlib.pyplot as plt

# Gate function g(t)
def g(t, D, H):
    return H * (np.abs(t) <= D / 2)

# a) DTFT function
def DTFT(nT, xn, w):
    Xw = np.array([np.sum(xn * np.exp(-1j * w_i * nT)) for w_i in w])
    return Xw

# Parameters
D = 8  # Duration
H = 2  # Height

# b) Sampling the gate function at different intervals T = D/80 and D/40
T1 = D / 80
T2 = D / 40

# Sampling time vectors
nT1 = np.arange(-D / 2, D / 2, T1)
nT2 = np.arange(-D / 2, D / 2, T2)

# Sampled signals
g1_n = g(nT1, D, H)
g2_n = g(nT2, D, H)

# Frequency vector for DTFT
w = np.linspace(-np.pi, np.pi, 1000)

# Calculate DTFTs of g1[n] and g2[n]
Gw1 = DTFT(nT1, g1_n, w)
Gw2 = DTFT(nT2, g2_n, w)

# Plot modulus and phase comparison for Gw1 and Gw2
fig, axs = plt.subplots(1, 2, figsize=(12, 6))

# Modulus
axs[0].plot(w, np.abs(Gw1), label="|Gw1| (T = D/80)")
axs[0].plot(w, np.abs(Gw2), label="|Gw2| (T = D/40)", linestyle="--")
axs[0].set_title("Modulus of DTFT for g1[n] and g2[n]")
axs[0].set_xlabel("Frequency ω (radians)")
axs[0].set_ylabel("Magnitude")
axs[0].legend()
axs[0].grid(True)

# Phase
axs[1].plot(w, np.angle(Gw1), label="Phase Gw1")
axs[1].plot(w, np.angle(Gw2), label="Phase Gw2", linestyle="--")
axs[1].set_title("Phase of DTFT for g1[n] and g2[n]")
axs[1].set_xlabel("Frequency ω (radians)")
axs[1].set_ylabel("Phase (radians)")
axs[1].legend()
axs[1].grid(True)

plt.tight_layout()
plt.show()

# c) Theoretical CTFT for g(t)
def CTFT(w, D, H):
    return H * np.sinc(w * D / (2 * np.pi))

# Frequency vector for theoretical CTFT comparison
w_ext = np.linspace(-3*np.pi, 3*np.pi, 1000)

# Calculate theoretical CTFT
G_theoretical = CTFT(w_ext, D, H)

# Plot comparison between CTFT and DTFTs
plt.figure(figsize=(10, 6))
plt.plot(w_ext, np.abs(G_theoretical), label="Theoretical CTFT", color="green")
plt.plot(w, np.abs(Gw1), label="|Gw1| (T = D/80)", linestyle="--")
plt.plot(w, np.abs(Gw2), label="|Gw2| (T = D/40)", linestyle="--", color="red")
plt.title("Comparison of CTFT and DTFT for g(t)")
plt.xlabel("Frequency ω (radians)")
plt.ylabel("Magnitude")
plt.legend()
plt.grid(True)
plt.show()

# d) Inverse DTFT for Gw1 and Gw2
# Corrected inverse DTFT function
def inverse_DTFT(Gw, w, nT):
    dt = w[1] - w[0]  # Frequency step size (Δω)
    x_reconstructed = np.array([np.sum(Gw * np.exp(1j * w * n_i)) * dt / (2 * np.pi) for n_i in nT])
    return x_reconstructed

# Reconstruct g1[n] and g2[n] using inverse DTFT
g1_reconstructed = inverse_DTFT(Gw1, w, nT1)
g2_reconstructed = inverse_DTFT(Gw2, w, nT2)

# Plot reconstructed signals and compare with original g1[n] and g2[n]
fig, axs = plt.subplots(1, 2, figsize=(12, 6))

# g1[n]
axs[0].plot(nT1, g1_n, label="Original g1[n]")
axs[0].plot(nT1, g1_reconstructed, label="Reconstructed g1[n]", linestyle="--")
axs[0].set_title("Comparison of Original and Reconstructed g1[n]")
axs[0].set_xlabel("n")
axs[0].set_ylabel("Amplitude")
axs[0].legend()
axs[0].grid(True)

# g2[n]
axs[1].plot(nT2, g2_n, label="Original g2[n]")
axs[1].plot(nT2, g2_reconstructed, label="Reconstructed g2[n]", linestyle="--")
axs[1].set_title("Comparison of Original and Reconstructed g2[n]")
axs[1].set_xlabel("n")
axs[1].set_ylabel("Amplitude")
axs[1].legend()
axs[1].grid(True)

plt.tight_layout()
plt.show()

# e) Parseval's relation: Compare energy in time and frequency domains
# Time-domain energy for g1[n] and g2[n]
energy_time_g1 = np.sum(np.abs(g1_n)**2) * (nT1[1] - nT1[0])
energy_time_g2 = np.sum(np.abs(g2_n)**2) * (nT2[1] - nT2[0])

# Frequency-domain energy for Gw1 and Gw2
energy_freq_g1 = np.sum(np.abs(Gw1)**2) * (w[1] - w[0]) / (2 * np.pi)
energy_freq_g2 = np.sum(np.abs(Gw2)**2) * (w[1] - w[0]) / (2 * np.pi)

# Print the energy results
print(f"Energy in time domain for g1[n]: {energy_time_g1}")
print(f"Energy in frequency domain for Gw1: {energy_freq_g1}\n")

print(f"Energy in time domain for g2[n]: {energy_time_g2}")
print(f"Energy in frequency domain for Gw2: {energy_freq_g2}")
