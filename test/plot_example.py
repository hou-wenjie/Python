import matplotlib.pyplot as plt
import numpy as np

# 生成数据
x = np.linspace(-10, 10, 100)
y = x ** 2

# 绘图
plt.plot(x, y, label="y = x²", color="blue")
plt.title("Simple Curve")
plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.grid(True)
plt.show()

