import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# plot data

# Series
# data=pd.Series(np.random.randn(1000),index=np.arange(1000))
# data=data.cumsum()
# data.plot()
# plot(x= ,y=)
# plt.show()

# DataFrame
# data=pd.DataFrame(np.random.randn(1000,4),index=np.arange(1000),columns=list("ABCD"))
# data=data.cumsum()
# print(data.head(5))

# data.plot() # plot里有非常多的参数
# plt.show()

# plot methods: 'bar','hist','box','kde','area','scatter','hexbin','pie', ...
# plt.scatter(x= , y= ) # 分布点图

# ax = data.plot.scatter(x='A',y='B',color='DarkBlue',label='Class 1')
# data.plot.scatter(x='A',y='C',color='DarkGreen',label='Class 2', ax=ax)
# plt.show()