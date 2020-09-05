import os
import csv
import pandas as pd

path="H:/cc/1-A04-李昂-动态_足印.csv"
path2="H:/cc/1-A04-李昂-动态_足印2.csv"
with open("C:/Users/ENERGY/Desktop/ppa.csv", 'r') as csvfile:
    reader = csv.reader(csvfile)
    rows = [row for row in reader]
print()
#      csvfile.close()
#        fo = open('test2.csv', 'wb')
#         fo.write(data.replace('\x00', ''))
#           fo.close()
# csvfile= open(path, 'r')
# reader = csv.reader(csvfile)
# rows = [row for row in reader]
# csvfile.close()