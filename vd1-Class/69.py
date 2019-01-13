"""
Viết chương trình sử dụng generator để in số chia hết cho 5 và 7 giữa 0 và n, cách nhau bằng dấu phẩy,
 n được người dùng nhập vào.

Ví dụ: Nếu n=100 được nhập vào thì đầu ra của chương trình là: 0,35,70.
"""
def numgenerator(n):
    for i in range(0, n+1):
        if i % 5 == 0 and i % 7 == 0:
            yield i
n = int(input("Nhập n: "))
lst = [str(x) for x in numgenerator(n)]
print("Các số chẵn: " + ", ".join(lst))

