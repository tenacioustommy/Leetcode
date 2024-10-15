import numpy as np
import matplotlib.pyplot as plt

# Given signal
L = 10
n = np.arange(L)
y_n = np.array([-1, 2, 3, 0, -2, 1, 4, -3, 0, -2])

# Plot y[n]
plt.figure(figsize=(10, 4))
plt.stem(n, y_n, basefmt=" ")
plt.title('Plot of y[n]')
plt.xlabel('n')
plt.ylabel('y[n]')
plt.xticks(n)
plt.grid()
plt.show()
# Frequency range
omega = np.linspace(-np.pi, np.pi, 1024)

# DTFT calculation
Y_omega = np.array([np.sum(y_n * np.exp(-1j * w * n)) for w in omega])

# Modulus and Phase
modulus = np.abs(Y_omega)
phase = np.angle(Y_omega)

# Plot modulus
plt.figure(figsize=(12, 6))

plt.subplot(2, 1, 1)
plt.plot(omega, modulus)
plt.title('Magnitude of DTFT Y(e^{jω})')
plt.xlabel('ω')
plt.ylabel('|Y(e^{jω})|')
plt.grid()

# Plot phase
plt.subplot(2, 1, 2)
plt.plot(omega, phase)
plt.title('Phase of DTFT Y(e^{jω})')
plt.xlabel('ω')
plt.ylabel('∠Y(e^{jω})')
plt.grid()

plt.tight_layout()
plt.show()
N = 10
Y_dft = np.fft.fft(y_n, N)

# Compare with DTFT
# Frequency bins for DFT
k = np.arange(N)
omega_k = 2 * np.pi * k / N

# Plotting
plt.figure(figsize=(12, 6))

plt.subplot(2, 1, 1)
plt.stem(omega_k, np.abs(Y_dft), basefmt=" ")
plt.title('Magnitude of DFT Y(jωk)')
plt.xlabel('ω')
plt.ylabel('|Y(jωk)|')
plt.grid()

plt.subplot(2, 1, 2)
plt.stem(omega_k, np.angle(Y_dft), basefmt=" ")
plt.title('Phase of DFT Y(jωk)')
plt.xlabel('ω')
plt.ylabel('∠Y(jωk)')
plt.grid()

plt.tight_layout()
plt.show()
y_idft = np.fft.ifft(Y_dft)

# Compare with y[n]plt.figure(figsize=(10, 4))
plt.stem(n, y_idft.real, basefmt=" ", label='Inverse DFT')
plt.stem(n, y_n, basefmt=" ", label='Original y[n]', linefmt='--')
plt.title('Comparison of Inverse DFT and Original y[n]')
plt.xlabel('n')
plt.ylabel('Amplitude')
plt.legend()
plt.grid()
plt.show()
L_new = 16
y_padded = np.pad(y_n, (0, L_new - L), 'constant')

# 16-point DFT
Y_16_dft = np.fft.fft(y_padded, L_new)

# Plotting results
plt.figure(figsize=(12, 6))
plt.subplot(2, 1, 1)
plt.plot(omega, np.abs(Y_omega), label='DTFT')
plt.stem(np.linspace(-np.pi, np.pi, L_new), np.abs(Y_16_dft), label='16-point DFT', basefmt=" ")
plt.title('Magnitude Comparison')
plt.xlabel('ω')
plt.ylabel('|Y|')
plt.legend()
plt.grid()

plt.subplot(2, 1, 2)
plt.plot(omega, phase, label='DTFT Phase')
plt.stem(np.linspace(-np.pi, np.pi, L_new), np.angle(Y_16_dft), label='16-point DFT Phase', basefmt=" ")
plt.title('Phase Comparison')
plt.xlabel('ω')
plt.ylabel('Phase')
plt.legend()
plt.grid()

plt.tight_layout()
plt.show()
import time

L_values = np.arange(1000, 10001, 1000)
dft_times = []
fft_times = []

for L in L_values:
    # Create random signal
    y_random = np.random.rand(L)
    
    # Measure DFT time
    start_time = time.time()
    np.fft.fft(y_random)  # Using FFT for DFT
    dft_times.append(time.time() - start_time)
    
    # Measure FFT time
    start_time = time.time()
    np.fft.fft(y_random)  # Using FFT directly
    fft_times.append(time.time() - start_time)

# Plotting the computational times
plt.figure(figsize=(10, 5))
plt.plot(L_values, dft_times, label='DFT Time', marker='o')
plt.plot(L_values, fft_times, label='FFT Time', marker='x')
plt.title('Computational Time of DFT and FFT')
plt.xlabel('L (Signal Length)')
plt.ylabel('Time (seconds)')
plt.legend()
plt.grid()
plt.show()
