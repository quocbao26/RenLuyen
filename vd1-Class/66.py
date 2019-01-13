"""
Dãy Fibonacci được tính dựa trên công thức sau:
f(n)=0 nếu n=0
f(n)=1 nếu n=1
f(n)=f(n-1)+f(n-2) nếu n>1
Hãy viết chương trình tính giá trị của f(n) với n là số được người dùng nhập vào.
Ví dụ: Nếu n được nhập vào là 7 thì đầu ra của chương trình sẽ là 13.
"""

def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)
n = int(input("Nhap n: "))
lst = [str(fib(x)) for x in range(0,n+1)]
print(' + '.join(lst))