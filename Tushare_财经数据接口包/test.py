import tushare as ts

# df = ts.get_index()
# print(df)
# print(type(df))

# profit = ts.profit_data(top=60)
# print(profit)

# repport = ts.forecast_data(2017, 4)
# print(repport)

sz_50 = ts.get_sz50s()
print(sz_50)

print(type(sz_50))
print(sz_50.iloc[7])
tz = sz_50.iloc[7]
print(type(tz))

print(ts.get_stock_basics())