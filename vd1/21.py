"""
Một website yêu cầu người dùng nhập tên người dùng và mật khẩu để đăng ký.
Viết chương trình để kiểm tra tính hợp lệ của mật khẩu mà người dùng nhập vào.

Các tiêu chí kiểm tra mật khẩu bao gồm:

1. Ít nhất 1 chữ cái nằm trong [a-z]
2. Ít nhất 1 số nằm trong [0-9]
3. Ít nhất 1 kí tự nằm trong [A-Z]
4. Ít nhất 1 ký tự nằm trong [$ # @]
5. Độ dài mật khẩu tối thiểu: 6
6. Độ dài mật khẩu tối đa: 12

Chương trình phải chấp nhận một chuỗi mật khẩu phân tách nhau bởi dấu phẩy và kiểm tra
 xem chúng có đáp ứng những tiêu chí trên hay không. Mật khẩu hợp lệ sẽ được in,
 mỗi mật khẩu cách nhau bởi dấu phẩy.

Ví dụ mật khẩu nhập vào chương trình là: ABd1234@1,a F1#,2w3E*,2We3345

Thì đầu ra sẽ là: ABd1234@1
"""
import string, re

lst_lower = list(string.ascii_lowercase)
lst_upper = list(string.ascii_uppercase)
lst_special = ['$', '#', '@']
arrHL = []
chuoi = input("Nhập chuỗi mật khẩu: ")
arrChuoi = chuoi.split(',')
for item in arrChuoi:
    chu_thuong = False
    chu_so = False
    chu_hoa = False
    ky_tu = False
    if len(item) < 6 or len(item) > 12:
        continue
    else:
        if re.search("[a-z]", item):
            chu_thuong = True
        if re.search("[A-Z]", item):
            chu_hoa = True
        if re.search("[0-9]", item):
            chu_so = True
        if re.search("[$#@]", item):
            ky_tu = True
        else:
            pass
    if chu_thuong == True and chu_hoa == True and chu_so == True and ky_tu == True:
        arrHL.append(item)
print("mật khẩu hợp lệ: ", ', '.join(arrHL))









