"""
Viết một chương trình để tạo tuple khác,
chứa các giá trị là số chẵn trong tuple (1,2,3,4,5,6,7,8,9,10) cho trước.
"""
tup = (1,2,3,4,5,6,7,8,9,10)
lst = []
for i in tup:
    if i % 2 == 0:
        lst.append(i)
print(tuple(lst))


