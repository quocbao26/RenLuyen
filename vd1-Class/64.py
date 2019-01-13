"""
Viết một chương trình tính 1/2 + 2/3 + 3/4 + ... + n/(n + 1) với một n là số được nhập vào (n> 0).
Ví dụ, nếu n là số sau đây được nhập vào:
5
Thì đầu ra phải là:
3.55
"""

i = int(input("Nhap so: "))
sum = 0.0
for i in range(1, i+1):
    sum += float(float(i)/(i+1))
print(round(sum,3))