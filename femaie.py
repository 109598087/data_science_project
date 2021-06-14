import pandas as pd

years = ['2010', '2012', '2013', '2014', '2015', '2016']

for year in years:
    # read data
    table = pd.read_csv(year + '.csv')

    # 缺失值 -> drop row
    table.dropna(inplace=True)

    # change dtype
    # print(table.columns)
    convert_dict = {'女董事': int,
                    '男董事': int,
                    'ROE': float,
                    'ROA': float,
                    "Tobin'sQ": float,
                    }
    for column in table.columns:
        if '人數' in column:
            convert_dict[column] = int
        elif '比例' in column:
            convert_dict[column] = float
        elif '年資' in column:
            convert_dict[column] = float
    # print(convert_dict)
    table = table.astype(convert_dict)
    # print(table.dtypes)

    # print(table['女董事'])
    print(table['女董事'].sum())
    print(table['女性董事比例'].sum())

