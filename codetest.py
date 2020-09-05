
import chardet

import os
import csv
import pandas as pd
#
# f = open("D:/工作文件2/DJJData/2019足底-2时点编程数据/2-A03-解浩-呼吸后自然闭眼静态.csv",'rb')
# data = f.read()
# print(chardet.detect(data))

# with open("D:/工作文件2/DJJData/2019足底-2时点编程数据/2-A03-解浩-自然左脚闭眼.csv", 'r') as csvfile:
with open("D:/工作文件2/DJJData/2019足底-2时点编程数据/2-A03-解浩-自然左脚闭眼.csv", 'r') as csvfile:
    # creating a csv reader object
    csvreader = csv.reader(csvfile)

    # extracting field names through first row
    fields = next(csvreader)

    # extracting each data row one by one
    for row in csvreader:
        print(row)
        # rows.append(row)
            #     if line_count == 0:
    #         print(f'Column names are {", ".join(row)}')
    #         line_count += 1
    #     # print(f'\t{row["name"]} works in the {row["department"]} department, and was born in {row["birthday month"]}.')
    #     # line_count += 1
    # print(f'Processed {line_count} lines.')
    # a=[line.decode('ascii').encode('utf-8') for line in csvfile]
    # reader = csv.reader((line.decode('GB2312').encode('utf-8') for line in csvfile), delimiter=",")
    # rows = [row for row in reader]

f = open("D:/工作文件2/DJJData/2019足底-2时点编程数据/2-A03-解浩-自然左脚闭眼.csv",'rb')
data = f.read()
print(chardet.detect(data))
#
# f = open("D:\工作文件2\DJJData\2019足底-2时点编程数据/2-A03-解浩-自然左脚闭眼.csv",'rb')
# data = f.read()
# print(chardet.detect(data))