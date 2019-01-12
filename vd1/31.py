"""
Định nghĩa hàm có thể chấp nhận input là số nguyên và
in "Đây là một số chẵn" nếu nó chẵn và in "Đây là một số lẻ" nếu là số lẻ.

Gợi ý:

Sử dụng toán tử % để kiểm tra xem số đó chẵn hay lẻ.
"""
def loai(n):
    if n % 2 == 0:
        print("Đây là số chẵn")
    elif n % 2 != 0:
        print("Đây là số lẻ")
so = int(input("Nhập số: "))
loai(so)