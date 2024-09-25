import pandas as pd
# df = pd.read_csv("https://github.com/dongupak/DataML/raw/main/csv/vehicle_prod.csv")
# df.to_csv("vehicle.csv", encoding='utf-8')
df = pd.read_csv("vehicle.csv", index_col=0)
print(df)
print(df.columns)
df_column_list = df.columns.to_list()
del(df_column_list[0])
print(df_column_list)
print(df.index)
print(df['2007'])
year_columns = [str(year) for year in range(2007, 2012)]
df['Total (2007-2011)'] = df[year_columns].sum(axis=1)
df['Mean (2007-2011)'] = df[year_columns].mean(axis=1)
print(df)

df.to_csv("NewData.csv", encoding="utf-8")