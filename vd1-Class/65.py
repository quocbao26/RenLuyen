"""
Viết chương trình tính:  f(n)=f(n-1)+100 khi n>0 và f(0)=1, với n là số được nhập vào (n>0).

Ví dụ: Nếu n được nhập vào là 5 thì đầu ra phải là 500.
"""
def f(n):
    if n == 0:
        return 0
    else:
        return f(n-1) + 100
n = int(input("Nhap n: "))
print(f(n))