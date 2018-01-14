import matplotlib.pyplot as plt
import numpy as np

n = 1024
X = np.random.normal(0, 1, n) # 平均值 0，方差 1
Y = np.random.normal(0, 1, n)
T = np.arctan2(Y, X) # for color value

plt.scatter(X, Y, s=75, c=T, alpha=0.5) # cmap 参数对应 c 使用
# plt.scatter(np.arange(5),np.arange(5)) # 一条线的散点图

plt.xlim((-1.5,1.5))
plt.ylim((-1.5,1.5))

plt.xticks(())
plt.yticks(())

plt.show()