import pandas as pd
import numpy as np

dates=pd.date_range('20130101',periods=6)
df=pd.DataFrame(np.arange(24).reshape(6,4),index=dates,columns=['A','B','C','D'])
df.iloc[0,1]=np.nan
df.iloc[1,2]=np.nan

print(df)

# 处理数据
# print(df.dropna(axis=0,how='any')) # 将缺失数据的行丢掉
#how={'any','all'} all 表示之后axis方向上所有都缺失才丢掉, any 只要出现就丢掉

# print(df.fillna(value=0)) # 填写NaN

# print(df.isnull()) #检查有没有NaN,返回True of False

# print(np.any(df.isnull()==True)) #缺失比较难找,至少有一个等于True