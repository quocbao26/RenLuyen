"""
Định nghĩa một hàm có thể tạo và in list chứa các giá trị bình phương của các số từ 1 đến 20 (tính cả 1 và 20).
"""
def inLIST():
    lst = []
    for i in range(1,21):
        lst.append(i**2)
    print(lst)
inLIST()



# và in 5 mục đầu tiên trong list.
def inLIST():
    lst = []
    for i in range(1,21):
        lst.append(i**2)
    print(lst[:5])
inLIST()

# in 5 mục cuối cùng trong list.
def inLIST():
    lst = []
    for i in range(1,21):
        lst.append(i**2)
    print(lst[-5:])
inLIST()

# in tất cả các giá trị của list, trừ 5 mục đầu tiên.
def inLIST():
    lst = []
    for i in range(1,21):
        lst.append(i**2)
    print(lst[5:])
inLIST()