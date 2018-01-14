import matplotlib.pyplot as plt
import numpy as np

x=np.linspace(-3,3,50)
y1=2*x+1
y2=x**2

plt.figure()
plt.plot(x,y2)
plt.plot(x,y1,color='red',linewidth=1.0,linestyle='--')

# x，y取值范围设置
plt.xlim((-1,2))
plt.ylim((-2,3))
# x，y标签设置
plt.xlabel('I am x')
plt.ylabel('I am y')
#设置x轴单位长度
new_ticks=np.linspace(-1,2,5)
print (new_ticks)
plt.xticks(new_ticks)
#设置y轴对应的内容
plt.yticks([-2, -1.8, -1, 1.22, 3],
[r'$really\ bad$', r'$bad\ \alpha$', r'$normal$', r'$good$', r'$really\ good$'])
plt.show()