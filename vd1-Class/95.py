"""
Viết chương trình nhận chuỗi đầu vào từ giao diện điều khiển và in nó theo thứ tự ngược lại.
Ví dụ nếu chuỗi nhập vào là:
i love you
Thì kết quả đầu ra là:
uoy evol i
"""
s = "i love you"
print(s[::-1])

#Viết chương trình nhận chuỗi do người dùng nhập vào và in các ký tự có chỉ số chẵn.
#Ví dụ: Nếu chuỗi sau được nhập vào: q1u2a3n4t5r6i7m8a9n4g5.6c7o8m, thì đầu ra sẽ là: quantrimang.com.
s = "q1u2a3n4t5r6i7m8a9n4g5.6c7o8m"
print(s[::2])