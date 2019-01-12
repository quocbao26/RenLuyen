import math

c = 50
h = 30
d = [x for x in input("Nhập giá trị: ").split(',')]

values = []
for i in d:
    values.append(str(int(round(math.sqrt(2 * c * float(i) / h)))))


print(','.join(values))
