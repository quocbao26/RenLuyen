"""
Định nghĩa 1 hàm có thể tạo và in một tuple
chứa các giá trị bình phương của các số từ 1 đến 20 (tính cả 1 và 20).
"""

def inTuple():
    lst = [x**2 for x in range(1,21)]
    print(tuple(lst))
inTuple()