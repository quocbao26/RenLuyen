"""
Viết chương trình in list sau khi xóa các số chẵn trong [5,6,77,45,22,12,24].
Sử dụng list comprehension để xóa một loạt phần tử của list.
"""
lst = [5,6,77,45,22,12,24]
print([x for x in lst if x % 2 != 0])

#Sử dụng list comprehension để
# viết chương trình in list sau khi đã loại bỏ các số chia hết cho 5 và 7 trong [12,24,35,70,88,120,155].
print([x for x in [12,24,35,70,88,120,155] if x % 5 != 0 and x % 7 ])

#Viết chương trình in list sau khi đã xóa số thứ 0, thứ 2, thứ 4, thứ 6 trong [12,24,35,70,88,120,155].
#enumerate lấy dc index, value
print([x for i,x in enumerate([12,24,35,70,88,120,155]) if x % 2 != 0])
