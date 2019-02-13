"""
Định nghĩa một class có ít nhất 2 method:

getString: để nhận một chuỗi do người dùng nhập vào từ giao diện điều khiển.

printString: in chuỗi vừa nhập sang chữ hoa.

Thêm vào các hàm hiểm tra đơn giản để kiểm tra method của class.

Ví dụ: Chuỗi nhập vào là quantrimang.com thì đầu ra phải là: QUANTRIMANG.COM
"""
class Chuoi:

    def __init__(self,chuoi):
        self.chuoi = chuoi

    def getString(self):
        print(self.chuoi.upper())

chuoi = Chuoi("quantrimang.com")
chuoi.getString()

print(int.__doc__)


