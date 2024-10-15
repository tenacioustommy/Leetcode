import numpy as np
import matplotlib.pyplot as plt

# Parameters
T = 0.01  # Sampling interval
fs = 100  # Sampling frequency
f1 = 16   # Frequency of first sine wave
A1 = 1.4  # Amplitude of first sine wave
f = 1     # Frequency offset
f2 = f1 + f  # Frequency of second sine wave
A2 = 0.6  # Amplitude of second sine wave

# DTFT function
def DTFT(x, N):
    w = np.linspace(-np.pi, np.pi, N)
    Xw = np.fft.fftshift(np.fft.fft(x, N))
    return w, Xw

# Generate the signal x(nT)
def generate_signal(L, T, f1, A1, f2, A2):
    n = np.arange(L)
    x = A1 * np.sin(2 * np.pi * f1 * n * T) + A2 * np.sin(2 * np.pi * f2 * n * T)
    return x

# Apply Hamming window
def apply_hamming_window(x):
    return x * np.hamming(len(x))

# Plot DTFT magnitude
def plot_dtft(w, Xw, L, title, f1, f2, A1, A2, factor):
    freqs = np.linspace(0, fs/2, len(Xw)//2)
    plt.figure(figsize=(10, 6))
    plt.plot(freqs, np.abs(Xw[:len(Xw)//2]) * factor)
    plt.title(f'{title} (L={L})')
    plt.xlabel('Frequency (Hz)')
    plt.ylabel('Magnitude')
    plt.axvline(x=f1, color='r', linestyle='--', label=f'f1 = {f1} Hz, A1 = {A1}')
    plt.axvline(x=f2, color='g', linestyle='--', label=f'f2 = {f2} Hz, A2 = {A2}')
    plt.legend()
    plt.grid(True)
    plt.show()

# Table 1: Original signal
L_values = [50, 200, 1000]
for L in L_values:
    # Generate signal
    x = generate_signal(L, T, f1, A1, f2, A2)
    
    # Compute DTFT
    w, Xw = DTFT(x, 2048)
    
    # Apply appropriate scaling factor
    factor = 1 / L
    
    # Plot DTFT and show f1, f2
    plot_dtft(w, Xw, L, 'DTFT of original signal', f1, f2, A1, A2, factor)

# Table 2: Hamming windowed signal
for L in L_values:
    # Generate signal
    x = generate_signal(L, T, f1, A1, f2, A2)
    
    # Apply Hamming window
    xw = apply_hamming_window(x)
    
    # Compute DTFT
    w, Xw_w = DTFT(xw, 2048)
    
    # Apply appropriate scaling factor
    factor = 1 / L
    
    # Plot DTFT and show f1, f2
    plot_dtft(w, Xw_w, L, 'DTFT of Hamming-windowed signal', f1, f2, A1, A2, factor)
