import numpy as np
import matplotlib.pyplot as plt

# 参数设置
A = 3  # 中心门函数宽度
B = 4  # 中心门函数高度
D = 8  # 门函数之间的距离

# 定义中心门函数 g_0(t)
def g0(t):
    if 0 <= t <= A:
        return B
    else:
        return 0

# 定义相邻门函数 g_1(t) 和 g_2(t)
def g1(t):
    return g0(3 * t + D)

def g2(t):
    return 2 * g0(t - D)

# 生成时间向量
t_min = -10
t_max = 15
t_step = 0.01
t = np.arange(t_min, t_max+t_step, t_step)

# 计算门函数值
g0_values = list(map(g0, t))
g1_values = list(map(g1, t))  # 限制 g1_values 的长度与 g0_values 相同
g2_values = list(map(g2, t))  # 限制 g2_values 的长度与 g0_values 相同

# 计算 x(t) = g0(t) + g1(t) + g2(t)
x_values = result = [sum(x) for x in zip(g0_values, g1_values, g2_values)]
# 绘制门函数和 x(t)
plt.figure(figsize=(10, 6))
# plt.plot(t, g0_values, label=r'$g_0(t)$')
# plt.plot(t, g1_values, label=r'$g_1(t)$')
# plt.plot(t, g2_values, label=r'$g_2(t)$')
plt.plot(t, x_values, label=r'$x(t)$')
plt.title('Signal Operations with Gate Functions')
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.legend()
plt.grid(True)
plt.show()