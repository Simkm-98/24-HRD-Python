from operator import index

import pandas as pd
#
# se = pd.Series([1, 2, None, 4], index= ['A','B','C','D'])
# print(se)
# print(se.isna())
# find = False
# if se.isna().any():
#     print("값이 없는게 있습니다.")
# else:
#     print("Missing Value 가 없습니다.")
#
# print(se['B'])
#
# income = { '1월':9500, '2월':6200, '3월':6050, '4월':7000}
# income_se = pd.Series(income)
# print('상점 수익')
# print(income_se)
# print(income_se['1월'])
#
#
# month_se = pd.Series(['1월','2월','3월','4월'])
# income_se = pd.Series([9500, 6200, 6050, 7000])
# expenses_se = pd.Series([5040, 2350, 2300, 4800])
# df = pd.DataFrame( {'월':month_se, '수익':income_se,'지출':expenses_se})
# print(df)
# print(df.iloc[0])

df = pd.read_csv("Hollys_table.csv", index_col=0)
print(df)
print(df.iloc[1])
print(df.head())
print(df.columns)
column_list = df.columns.to_list()
print(column_list)
name = '매장'
if name in df.columns:
    print("매장을 찾았습니다")
df['Total'] = df.columns.name
print(df)