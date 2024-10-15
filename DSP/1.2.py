import numpy as np
import matplotlib.pyplot as plt

# 参数设置
fs = 100  # 采样率
t = np.arange(0, 5, 1/fs)  # 时间向量
f1 = 800  # 第一个谐波频率
f2 = 850  # 第二个谐波频率
A1 = 1  # 第一个谐波幅度
A2 = 1  # 第二个谐波幅度

# 生成连续时间信号 x(t)
x = A1 * np.sin(2 * np.pi * f1 * t) + A2 * np.sin(2 * np.pi * f2 * t)

# 计算 CTFT
def CTFT(x):
    T = len(x) / fs
    Xw = np.fft.fftshift(np.fft.fft(x)) / fs
    return Xw

Xw = CTFT(x)

# 绘制 CTFT
plt.figure(figsize=(10, 6))
plt.plot(Xw.imag, label='CTFT of x(t)')
plt.title('CTFT of x(t)')
plt.xlabel('Frequency (Hz)')
plt.ylabel('Amplitude')
plt.legend()
plt.grid(True)
plt.show()
