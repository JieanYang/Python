# 使用 SciPy 和 NumPy 表明概率密度函数。
# 首先用 SciPy 中的 norm() 创建正态分布样本
# 而后用 NumPy 中的 hstack() 进行水平方向上的堆叠，并应用 SciPy 中的 gaussian_kde()

from scipy.stats.kde import gaussian_kde
from scipy.stats import norm
from numpy import linspace, hstack
from pylab import plot, show, hist
import matplotlib.pyplot as plt

sample1 = norm.rvs(loc=-1.0, scale=1, size=320)
sample2 = norm.rvs(loc=2.0, scale=0.6, size=320)
sample = hstack([sample1, sample2])
probDensityFun = gaussian_kde(sample)
print(probDensityFun)
plt.title("KDE Demonstration using Scipy and Numpy", fontsize=20)
x = linspace(-5, 5, 200)
print(probDensityFun(x))
plot(x, probDensityFun(x), 'r')
hist(sample, normed=1, alpha=0.45, color='purple')
show()