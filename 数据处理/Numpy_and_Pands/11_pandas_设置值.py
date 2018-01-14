import pandas as pd
import numpy as np

dates=pd.date_range('20130101',periods=6)
df=pd.DataFrame(np.arange(24).reshape((6,4)), index=dates,columns=['A','B','C','D'])
print(df)

df.iloc[2,2]=1111
df.loc['20130101','B']=2222
df.ix[1,'D']=3333
df[df.A>4]=0 # 对A列里，大于4的行的数值都转化为0
df.A[df.A<4]=1 # 对A列里，大于4的的数值都转化为1
df['F']=np.nan # 增加空的列
df['E']=pd.Series([1,2,3,4,5,6],index=dates)
print(df)