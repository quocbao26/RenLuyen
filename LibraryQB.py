
import random, json

# ------------------ Tạo list trong khoảng với số chẵn hoặc lẻ --------------
#Vui lòng viết chương trình để tạo một list với 5 số chẵn từ 100 đến 200.
def dsSoChanTrongKhoang(start, end, n):
     return random.sample([x for x in range(start,end + 1) if x % 2 == 0], n) # return về 1 list

#Vui lòng viết chương trình để tạo một list với 5 số lẻ từ 100 đến 200.
def dsSoLeTrongKhoang(start, end, n):
    return random.sample([x for x in range(start, end + 1) if x % 2 != 0], n) # return về 1 list

# ------------------ Đọc ghi file json --------------
# Đọc file json
def docFile(path):
    file = open(path, encoding='utf-8')
    data = json.load(file)
    file.close()
    return data

# Ghi file json
def ghiFile(path, noidung):
    file = open(path, 'w',encoding='utf-8')
    json.dump(noidung, file, indent=4, ensure_ascii=False)
    file.close()
    return 1