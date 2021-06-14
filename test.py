import pandas as pd

# read data
table_2010 = pd.read_csv('2010.csv')

columns = table_2010.columns

table_2010.dropna(inplace=True)

print(table_2010)
# for row in table_2010['ROA']:
#     print(row.index)
#     print(float(row))

# # change dtype
# convert_dict = {'女董事': int,
#                 '男董事': int,
#                 'ROE': float,
#                 'ROA': float,
#                 # "Tobin's Q": float,
#                 # '公司治理等級': int
#                 }
# print(table_2010['ROA'].values)
