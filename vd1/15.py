"""
Viết một chương trình tìm tất cả các số trong đoạn 1000 và 3000 (tính cả 2 số này)
sao cho tất cả các chữ số trong số đó là số chẵn.
In các số tìm được thành chuỗi cách nhau bởi dấu phẩy, trên một dòng.
"""
values = []
for i in range(2000, 3001):
    if i % 2 == 0:
        values.append(str(i))
print(', '.join(values))



