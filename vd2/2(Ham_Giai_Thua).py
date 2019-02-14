"""
Viết một chương trình có thể tính giai thừa của một số cho trước.
Kết quả được in thành chuỗi trên một dòng, phân tách bởi dấu phẩy.
Ví dụ, số cho trước là 8 thì kết quả đầu ra phải là 40320.
"""
from math import *


def fact(n):
    if n <= 1:
        return 1
    return n * fact(n - 1)


so = int(input("Nhập số: "))
kq = fact(so)
kq1 = factorial(so)
print(kq, kq1)
