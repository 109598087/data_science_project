import pandas as pd
import matplotlib.pyplot as plt
from numpy.polynomial.polynomial import polyfit
import numpy as np

plt.rcParams['font.sans-serif'] = ['Microsoft JhengHei']
plt.rcParams['axes.unicode_minus'] = False


def get_polyfit(data):
    x = np.array(years_num)
    y = np.array(data)
    b, m = polyfit(x, y, 1)
    plt.plot(x, m * x + b, linestyle='--')
    return b, m


def get_corr_plot(table_list, column_name, tse_oct):
    tse_ROE_corr = list()
    tse_ROA_corr = list()
    tse_tobin_corr = list()
    for table in table_list:
        tse = table[table['上市別'] == tse_oct]
        tse_corr = tse.corr()
        tse_ROE_corr.append(tse_corr[column_name]['ROE'])
        tse_ROA_corr.append(tse_corr[column_name]['ROA'])
        tse_tobin_corr.append(tse_corr[column_name]["Tobin'sQ"])
    plt.plot(years_num, tse_ROE_corr, label='ROE')
    plt.plot(years_num, tse_ROA_corr, label='ROA')
    plt.plot(years_num, tse_tobin_corr, label="Tobin'sQ")
    get_polyfit(tse_ROE_corr)
    get_polyfit(tse_ROA_corr)
    get_polyfit(tse_tobin_corr)

    plt.xlabel('year')
    plt.ylabel('碩博士董事比例與公司績效之' + '相關係數')
    plt.title('在上市公司，' + '女性碩博士董事比例' + '與公司績效之相關係數，隨年份變化趨勢圖')
    plt.legend()
    plt.show()


def get_sum_plot(table_list, column_name):
    TSE_list = list()
    OTC_list = list()
    all_list = list()

    for table in table_list:
        # change dtype
        convert_dict = {column_name: float}
        table = table.astype(convert_dict)

        # print(table.dtypes)
        TSE_list.append(table[table['上市別'] == 'TSE'][column_name].sum())
        OTC_list.append(table[table['上市別'] == 'OTC'][column_name].sum())
        all_list.append(table[column_name].sum())

    plt.plot(years, TSE_list, label='TSE')
    plt.plot(years, OTC_list, label='OTC')
    plt.plot(years, all_list, label='all')
    plt.xlabel('year')
    plt.ylabel(column_name + 'number')
    plt.title('rename')
    plt.legend()
    plt.show()


def get_mean_plot(table_list, column_name):
    TSE_list = list()
    OTC_list = list()
    all_list = list()

    for table in table_list:
        # change dtype
        convert_dict = {column_name: float}
        table = table.astype(convert_dict)

        # print(table.dtypes)
        TSE_list.append(table[table['上市別'] == 'TSE'][column_name].mean())
        OTC_list.append(table[table['上市別'] == 'OTC'][column_name].mean())
        all_list.append(table[column_name].mean())

    plt.plot(years, TSE_list, label='TSE')
    plt.plot(years, OTC_list, label='OTC')
    plt.plot(years, all_list, label='all')
    plt.xlabel('year')
    plt.ylabel('number')
    plt.title(column_name)
    plt.legend()
    plt.show()


years = ['2010', '2012', '2013', '2014', '2015', '2016']
years_num = [2010, 2012, 2013, 2014, 2015, 2016]
# 得到所有年分都有的公司s
all_company_name_list = list()
for year in years:
    table = pd.read_csv(year + '.csv')
    table.dropna(inplace=True)
    all_company_name_list.append(table['簡稱'].values)

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
print(len(table_list[0][table_list[0]['上市別'] == 'TSE']))
print(len(table_list[0][table_list[0]['上市別'] == 'OTC']))
# print(table_list)


# get_sum_plot(table_list, '女董事')
# # get_sum_plot(table_list, '男董事')
# get_sum_plot(table_list, '董事總人數')
#
# get_mean_plot(table_list, '女性董事比例')
# #
# # 計算相關係數
# get_corr_plot(table_list, '女董事', 'TSE')
# get_corr_plot(table_list, '女董事', 'OTC')

# get_corr_plot(table_list, '女性董事比例', 'TSE')

# get_corr_plot(table_list, '董事碩士加博士比例', 'TSE')
# get_corr_plot(table_list, '董事碩士加博士比例', 'TSE')
#
get_corr_plot(table_list, '女性董事碩加博士比例', 'TSE')
# get_corr_plot(table_list, '女性高中職以下學位董事比例', 'TSE')
#
# get_corr_plot(table_list, '平均年資', 'TSE')
# get_corr_plot(table_list, '女性平均年資', 'TSE')


# # 最適合比例
# table_ = table_list[5]
# ROE_female_radio_dict = dict()
# female_list = table_['女性平均年資'].values
# ROE_list = table_['ROE'].values
# for i in range(len(female_list)):
#     ROE_female_radio_dict[female_list[i]] = ROE_list[i]
# print(ROE_female_radio_dict)
# temp = [(k, ROE_female_radio_dict[k]) for k in sorted(ROE_female_radio_dict.keys())]
#
# temp_list_key = list()
# temp_list_value = list()
# for i in range(len(temp)):
#     if len(temp) != 0:
#         temp_list_key.append(temp[i][0])
#         temp_list_value.append(temp[i][1])
# print(temp_list_key)
# plt.plot(temp_list_key, temp_list_value)
# plt.show()
