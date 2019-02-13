"""
Với 2 list cho trước: [1,3,6,78,35,55] và [12,24,35,24,88,120,155],
 viết chương trình để tạo list có phần tử là giao của 2 list đã cho.
"""
lst1 = [1,3,6,78,35,55]
lst2 = [12,24,35,24,88,120,155]
lst3 = set(lst1) & set(lst2)
print(lst3)


#Viết chương trình in list từ list [12,24,35,24,88,120,155,88,120,155],
# sau khi đã xóa hết các giá trị trùng nhau.
lst3 = set(lst1) ^ set(lst2)
print(lst3)