"""
Viết một chương trình chấp nhận đầu vào là một câu, đếm số chữ cái và chữ số trong câu đó.
 Giả sử đầu vào sau được cấp cho chương trình: hello world! 123

Thì đầu ra sẽ là:

Số chữ cái là: 10
Số chữ số là: 3
"""
chuoi = input("Chuỗi: ")
chu = 0
so = 0
for i in chuoi:
    if i.isalpha():
        chu += 1
    elif i.isdigit():
        so += 1
print("Số chữ cái là:", chu)
print("Số chữ số là:", so)




