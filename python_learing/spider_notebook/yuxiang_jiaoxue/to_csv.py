'''
CSV(Comma Separator Value):逗号分隔符
CSV文件是有任意的数据记录组成,记录检以某种换行符分隔,每行记录有换行符组合
ID, Username, Age, Country
1001, dana, 18, China
1002, huanglaoban, 28, China
'''

import csv

headers = ['ID', 'Userename', 'Age', 'Country']
rows = [
    (1001, 'Liudana', 18, 'BeiJing'),
    (1002, 'huanglaoban', 28, 'ChengDu'),
    (1003, 'yitengjun', 'Nan', 'Jinan')
]

with open('../datas/tables/test.csv', 'w') as f:
    f_csv = csv.writer(f)
    f_csv.writerow(headers)
    f_csv.writerows(rows)
