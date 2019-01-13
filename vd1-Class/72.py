"""
Viết hàm tìm kiếm nhị phân để tìm các item trong một list đã được sắp xếp.
Hàm sẽ trả lại chỉ số của phần tử được tìm thấy trong list.
"""
import math


def seach_Binary(lst, x):
    left = 0
    right = len(lst)-1
    index = -1
    while right >= left and index == -1:
        mid = int((left+right)/2.0)
        if lst[mid] == x:
            index = mid
        elif lst[mid] < x:
            left = mid + 1
        else:
            right = mid - 1
    return index
lst=[2,5,7,9,11,17,222]
print (seach_Binary(lst,11))
print (seach_Binary(lst,12))