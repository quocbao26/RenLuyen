"""
tạo ra một dictionary chứa (i, i*i) như là số nguyên từ 1 đến n
(bao gồm cả 1 và n) sau đó in ra dictionary này.
Ví dụ: Giả sử số n là 8 thì đầu ra sẽ là: {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64}.
"""
dic = {}
n = int(input("Nhap n:"))
for i in range(1, n+1):
    dic[i] = i**2
print(dic)

