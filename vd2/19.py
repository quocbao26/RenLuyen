"""
Sử dụng một danh sách để lọc các số lẻ từ danh sách được người dùng nhập vào.
Giả sử đầu vào là: 1,2,3,4,5,6,7,8,9 thì đầu ra phải là: 1,3,5,7,9
"""
chuoi = "1,2,3,4,5,6,7,8,9"
value = [x for x in chuoi.split(',') if int(x) % 2 != 0]
# for i in chuoi.split(","):
#     if int(i) % 2 != 0:
#         value.append(i)
print("Các số lẻ:", ','.join(value))