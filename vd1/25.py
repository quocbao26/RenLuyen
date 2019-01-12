"""
Viết chương trình tính tần suất các từ từ input. Output được xuất ra sau khi đã sắp xếp theo bảng chữ cái.

Giả sử input là: New to Python or choosing between Python 2 and Python 3? Read Python 2 or Python 3.
"""
import csv
s = "New to Python or choosing between Python 2 and Python 3? Read Python 2 or Python 3"
#Cách 2
s = s.split(" ")
dem = 0
dic = {}
for i in range(len(s)):
    for j in range(len(s)):
        if s[i] == s[j]:
            dem += 1
    dic[s[i]] = dem
    dem = 0
lstTu = list(dic.keys())
lstDem = list(dic.values())

for i in range(len(lstTu)):
    print(lstTu[i] + " - " + str(lstDem[i]))










#Cách 1
# tach_chuoi = s.split()
# data = []
# for tu in tach_chuoi:
#     dem_tu = tach_chuoi.count(tu)
#     chuoi = tu + " " + str(dem_tu)
#     #print(tu + " " + str(dem_tu))
#     tao_list = chuoi.split()
#     data.append(tao_list)
#
# f = open("count.csv", 'w', encoding='utf-8', newline="")
# for item in data:
#     csv.writer(f).writerow(item)
# f.close()
