"""
Viết một chương trình chấp nhận đầu vào là một câu, đếm chữ hoa, chữ thường.
Giả sử đầu vào là: Quản Trị Mạng

Thì đầu ra là:
Chữ hoa: 3
Chữ thường: 8
"""
chuoi = "Quản Trị Mạng"
dic = {"UPPER": 0, "LOWER": 0}
for i in chuoi:
    if i.isupper():
        dic['UPPER'] += 1
    elif i.islower():
        dic['LOWER'] += 1
print("Chữ hoa:", dic['UPPER'])
print("Chữ thường:", dic['LOWER'])