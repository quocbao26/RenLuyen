"""
Viết chương trình in list sau khi xóa các số chẵn trong [5,6,77,45,22,12,24].
Sử dụng list comprehension để xóa một loạt phần tử của list.
"""
lst = [5,6,77,45,22,12,24]
print([x for x in lst if x % 2 != 0])