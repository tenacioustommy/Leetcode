import numpy as np
import soundfile as sf
from matplotlib import pyplot as plt

"""Input the tone and sampling frequencies and check legal values."""
f0_str = input("Input the frequency of the pure tone,"
               " Enter for '1000' Hz: ")
if f0_str == '':
    f0_str = '1000'    # default sampling frequency

fs_str = input("Input the sampling frequencies, "
               "Enter for '44000' Hz: ")
if fs_str == '':
    fs_str = '44000'    # default sampling frequency

try:
    f0 = abs(int(f0_str))   # integer positive frequency
    fs = abs(int(fs_str))
    period = 1 / f0
except ValueError as e:
    print(f"Convert Input number error: {e}！")
    quit()
except ZeroDivisionError:
    print("Input number cannot be Zero！")
    quit()

"""A pure tone DT wave, may be aliasing."""
amp = 0.8
dt = 1 / fs
duration = 2
tt_d = np.arange(0, duration + dt, dt)
xt_d = amp * np.sin(2 * np.pi * f0 * tt_d)
# corresponding CT wave with a high sampling rate
fs_c = 100_000
dt_c = 1 / fs_c
tt_c = np.arange(0, duration + dt_c, dt_c)
xt_c = amp * np.sin(2 * np.pi * f0 * tt_c)

# Check aliasing.
if f0 < fs/2:
    aliasing = False
    fa = 0
else:
    aliasing = True
    fa = f0     # aliasing frequency
    while fa > fs/2:
        fa -= fs
        fa = abs(fa)
    print(f"Aliasing frequency: fa = {fa}")

"""Write the wave into a WAV file."""
filename = f"pure{f0}_fs{fs}_fa{fa}.wav"
sf.write(filename, xt_d, fs)
print(f"Create sound in {filename}.")

"""Plot results."""
# figure style and size
plt.style.use('bmh')
plt.figure(figsize=(8, 6))
plt.grid(False)

# time-domain
num_show_periods = 10
plt.title(f"f0 = {f0}, fs = {fs}, fa = {fa}", fontsize=12)
plt.plot(tt_d, xt_d, linewidth=2, linestyle='--')
plt.scatter(tt_d, xt_d, c='red', s=10)
plt.plot(tt_c, xt_c, c=(0.5, 0.5, 0.5), linewidth=0.5)
plt.xlim([min(tt_d), num_show_periods * period])
plt.xlabel('Time', fontsize=10)
plt.ylabel('x', fontsize=10)

# show plots
plt.show()
