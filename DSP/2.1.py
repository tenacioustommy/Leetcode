import numpy as np
import matplotlib.pyplot as plt

# Parameters
D = 8  # Duration
H = 5  # Height
t = np.arange(-D, D, 0.001)  # Time vector

# Gate function g(t)
def g(t, D, H):
    return H * (np.abs(t) <= D/2)

# a) Continuous-time Fourier transform (CTFT) function
def CTFT(x, t, w):
    dt = t[1] - t[0]
    Xw = np.array([np.sum(x * np.exp(-1j * w_i * t) * dt) for w_i in w])
    return Xw

# Gate function
g_t = g(t, D, H)

# b) Time shift of g(t), g2(t) = g(t - D/4)
shift = D / 4
g2_t = g(t - shift, D, H)

# Plot g(t) and g2(t)
plt.figure(figsize=(10, 6))
plt.plot(t, g_t, label="g(t)")
plt.plot(t, g2_t, label="g2(t) = g(t - D/4)", linestyle="--")
plt.title("Comparison of g(t) and g2(t)")
plt.xlabel("Time t")
plt.ylabel("Amplitude")
plt.legend()
plt.grid(True)
plt.show()

# Let's continue with the rest of the steps.
# c) Calculate CTFT of g(t) and g2(t) over w = -10 to 10
w = np.linspace(-10, 10, 1000)  # Frequency vector

# Calculate CTFTs
Gw = CTFT(g_t, t, w)
Gw2 = CTFT(g2_t, t, w)

# Plot comparison of modulus and phase of Gw and Gw2
fig, axs = plt.subplots(2, 2, figsize=(12, 8))

# Magnitude
axs[0, 0].plot(w, np.abs(Gw), label="|Gw|")
axs[0, 0].plot(w, np.abs(Gw2), label="|Gw2|", linestyle="--")
axs[0, 0].set_title("Magnitude of Gw and Gw2")
axs[0, 0].set_xlabel("Frequency w")
axs[0, 0].set_ylabel("Magnitude")
axs[0, 0].legend()
axs[0, 0].grid(True)

# Phase
axs[0, 1].plot(w, np.angle(Gw), label="Phase Gw")
axs[0, 1].plot(w, np.angle(Gw2), label="Phase Gw2", linestyle="--")
axs[0, 1].set_title("Phase of Gw and Gw2")
axs[0, 1].set_xlabel("Frequency w")
axs[0, 1].set_ylabel("Phase (radians)")
axs[0, 1].legend()
axs[0, 1].grid(True)

# Real part
axs[1, 0].plot(w, np.real(Gw), label="Real(Gw)")
axs[1, 0].plot(w, np.real(Gw2), label="Real(Gw2)", linestyle="--")
axs[1, 0].set_title("Real part of Gw and Gw2")
axs[1, 0].set_xlabel("Frequency w")
axs[1, 0].set_ylabel("Real")
axs[1, 0].legend()
axs[1, 0].grid(True)

# Imaginary part
axs[1, 1].plot(w, np.imag(Gw), label="Imag(Gw)")
axs[1, 1].plot(w, np.imag(Gw2), label="Imag(Gw2)", linestyle="--")
axs[1, 1].set_title("Imaginary part of Gw and Gw2")
axs[1, 1].set_xlabel("Frequency w")
axs[1, 1].set_ylabel("Imaginary")
axs[1, 1].legend()
axs[1, 1].grid(True)

plt.tight_layout()
plt.show()
# d) Define g3(t) = g(t) * cos(2t) and compare g(t) and g3(t) over t = [-15, 15]
t_extended = np.arange(-15, 15, 0.001)

# Define g3(t) = g(t) * cos(2t)
g3_t = g(t_extended, D, H) * np.cos(2 * t_extended)

# Compare g(t) and g3(t)
plt.figure(figsize=(10, 6))
plt.plot(t_extended, g(t_extended, D, H), label="g(t)")
plt.plot(t_extended, g3_t, label="g3(t) = g(t) * cos(2t)", linestyle="--")
plt.title("Comparison of g(t) and g3(t) over [-15, 15]")
plt.xlabel("Time t")
plt.ylabel("Amplitude")
plt.legend()
plt.grid(True)
plt.show()

# e) Compare the CTFT of g3(t) and g(t) in w = [-10, 10]
Gw3 = CTFT(g3_t, t_extended, w)

# Plot modulus and phase of CTFT for g(t) and g3(t)
fig, axs = plt.subplots(1, 2, figsize=(12, 6))

# Modulus
axs[0].plot(w, np.abs(Gw), label="|Gw|")
axs[0].plot(w, np.abs(Gw3), label="|Gw3|", linestyle="--")
axs[0].set_title("Modulus of CTFT for g(t) and g3(t)")
axs[0].set_xlabel("Frequency w")
axs[0].set_ylabel("Magnitude")
axs[0].legend()
axs[0].grid(True)

# Phase
axs[1].plot(w, np.angle(Gw), label="Phase Gw")
axs[1].plot(w, np.angle(Gw3), label="Phase Gw3", linestyle="--")
axs[1].set_title("Phase of CTFT for g(t) and g3(t)")
axs[1].set_xlabel("Frequency w")
axs[1].set_ylabel("Phase (radians)")
axs[1].legend()
axs[1].grid(True)

plt.tight_layout()
plt.show()
# f) Calculate energy of g3(t) in both time and frequency domains (Parseval's theorem)

# Energy in time domain (integral of |g3(t)|^2)
energy_time = np.sum(np.abs(g3_t) ** 2) * (t_extended[1] - t_extended[0])

# Energy in frequency domain (integral of |Gw3(w)|^2)
energy_freq = np.sum(np.abs(Gw3) ** 2) * (w[1] - w[0]) / (2 * np.pi)

print(energy_time, energy_freq)
