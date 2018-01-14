import matplotlib.pyplot as plt
import numpy as np

x=np.linspace(-3,3,50)
y1=2*x+1
y2=x**2

plt.figure()

# x，y取值范围设置
plt.xlim((-1,2))
plt.ylim((-2,3))
# x，y标签设置
plt.xlabel('I am x')
plt.ylabel('I am y')
# 设置x轴单位长度
new_ticks=np.linspace(-1,2,5)
print (new_ticks)
plt.xticks(new_ticks)
# 设置y轴对应的内容
plt.yticks([-2, -1.8, -1, 1.22, 3],
[r'$really\ bad$', r'$bad\ \alpha$',
 r'$normal$', r'$good$', r'$really\ good$'])

# 逗号是matplotlib里约定好的，为了能给handles使用
l1,=plt.plot(x,y2,label='up')
l2,=plt.plot(x,y1,color='red',linewidth=1.0,linestyle='--',label='down')
# 参数：handles,labels,loc
# handle 给线的样式
# loc=['best', 'upper right', ... ]
plt.legend(handles=[l1,l2],labels=['aaa','bbb'],loc='best')

plt.show()