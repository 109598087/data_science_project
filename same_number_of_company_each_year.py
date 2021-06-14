import pandas as pd

years = ['2010', '2012', '2013', '2014', '2015', '2016']
# 得到所有年分都有的公司s
all_company_name_list = list()
for year in years:
    table = pd.read_csv(year + '.csv')
    table.dropna(inplace=True)
    all_company_name_list.append(table['簡稱'].values)

# print(all_company_name_list)
final_company_list = list()

for company_name_2020 in all_company_name_list[1]:
    company_name_count = 0
    for all_company_name in all_company_name_list:
        for company_name in all_company_name:
            if company_name_2020 == company_name:
                company_name_count += 1
    if company_name_count == len(all_company_name_list):
        final_company_list.append(company_name_2020)
print(final_company_list)
print(len(final_company_list))

# 建立所有年份都有的公司的table
table_list = list()
for year in years:
    table = pd.read_csv(year + '.csv')
    for company_name_in_2010 in table['簡稱']:
        if company_name_in_2010 not in final_company_list:
            table.drop(table[table['簡稱'] == company_name_in_2010].index, inplace=True)
    table_list.append(table)

# print(table_list)


# change dtype
# print(table.columns)
for table in table_list:
    # change dtype
    convert_dict = {'女董事': int}
    table = table.astype(convert_dict)

    # print(table.dtypes)
    print(table['女董事'].sum())
