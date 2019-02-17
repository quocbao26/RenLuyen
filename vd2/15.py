"""
Viết một chương trình tìm tất cả các số trong đoạn 1000 và 3000 (tính cả 2 số này)
sao cho tất cả các chữ số trong số đó là số chẵn.
In các số tìm được thành chuỗi cách nhau bởi dấu phẩy, trên một dòng.
"""
value = []
for i in range(1000, 3001,2):
    value.append(str(i))
print(",".join(value))

