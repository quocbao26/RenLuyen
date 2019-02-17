"""
Viết một chương trình chấp nhận đầu vào là một câu, đếm số chữ cái và chữ số trong câu đó.
Giả sử đầu vào sau được cấp cho chương trình:
hello world! 123

Thì đầu ra sẽ là:
Số chữ cái là: 10
Số chữ số là: 3
"""
chuoi = "hello world! 123"
i = 0
j = 0

for character in chuoi:
    if character.isdigit():
        i += 1
    elif character.isalpha():
        j += 1
print("Số chữ cái là:", j)
print("Số chữ số là:", i)