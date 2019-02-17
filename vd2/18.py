"""
Viết một chương trình tính giá trị của a+aa+aaa+aaaa với a là số được nhập vào bởi người dùng.

Giả sử a được nhập vào là 1 thì đầu ra sẽ là: 1234
"""
n = int(input("Nhập n: "))
int1 = int("%i" % n)

int2 = int("%i%i" % (n,n))
int3 = int("%i%i%i" % (n,n,n))
int4 = int("%i%i%i%i" % (n,n,n,n))
print("Tổng:", int1+int2+int3+int4)