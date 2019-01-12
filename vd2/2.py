"""
Viết một chương trình có thể tính giai thừa của một số cho trước.
Kết quả được in thành chuỗi trên một dòng, phân tách bởi dấu phẩy.
Ví dụ, số cho trước là 8 thì kết quả đầu ra phải là 40320.
"""

chuoi = []
def fact(n):
    if n <= 1:
        chuoi.append(n)
        return 1
    chuoi.append(n)
    return n * fact(n - 1), chuoi


so = int(input("Nhập số: "))
kq, arr = fact(so)
print(", ".join(arr))
print(kq)
