"""
Định nghĩa một hàm có thể in dictionary chứa key là các số từ 1 đến 3
(bao gồm cả hai số) và các giá trị bình phương của chúng.

Gợi ý:

Sử dụng dict[key]=value để nhập mục vào dictionary.
Sử dụng toán từ ** để lấy bình phương của một số.
"""
def printDic():
    dic = dict()
    for i in range(1,21):
        dic[i] = i**2
    print(dic)
printDic()

# chỉ in giá trị
def printDic1():
    dic = dict()
    for i in range(1,21):
        dic[i] = i**2
    # for i in range(1,21):
    #     print(dic[i], end=" - ")
    for k, v in dic.items():
        print(v, end= " - ")
    for k, v in dic.items():
        print(k, end= " - ")
printDic1()