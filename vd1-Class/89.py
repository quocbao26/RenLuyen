"""
Viết chương trình in list sau khi đã xóa số ở vị trí thứ 0, thứ 4, thứ 5 trong [12,24,35,70,88,120,155].
"""
# Cách 1
lst = [12,24,35,70,88,120,155]
print([lst[x] for x in range(len(lst)) if x % 5 != 0])

# Cách 2
print([value for key, value in enumerate(lst) if key not in (0, 4, 5)])
print(lst)

#Viết chương trình in list sau khi đã xóa giá trị 24 trong [12,24,35,24,88,120,155].
#Cách 1 : có mảng mới
arr = [12,24,35,24,88,120,155]
print([x for x in arr if x != 24])
print(arr)
#Cách 2: giữ mảng cũ
for i in arr:
    if i == 24:
        arr.remove(i)
print(arr)