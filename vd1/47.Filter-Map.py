"""
Viết chương trình Python dùng map() và filter()
 để tạo list chứa giá trị bình phương của các số chẵn trong [1,2,3,4,5,6,7,8,9,10].
"""
lst = [1,2,3,4,5,6,7,8,9,10]
arr = list(map(lambda x: x**2, list(filter(lambda x: x % 2 == 0, lst))))
print(arr)

#Viết chương trình Python dùng filter() để tạo danh sách chứa các số chẵn trong đoạn [1,20].
print(list(filter(lambda x: x % 2 == 0, range(1,21))))
#Viết chương trình Python sử dụng map() để tạo list chứa giá trị bình phương của các số trong đoạn [1,20].
print(list(map(lambda x: x**2, range(1,21))))