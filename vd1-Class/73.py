"""
Tạo một số thập phân ngẫu nhiên,
có giá trị nằm trong khoảng từ 10 đến 100 bằng cách sử dụng module math của Python.
"""
import random
for i in range(1,11):
    print(round(random.random()*100-5,1), end=" - ")

