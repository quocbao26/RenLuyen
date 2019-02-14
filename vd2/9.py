"""
Viết chương trình và in giá trị theo công thức cho trước:
 Q = √([(2 * C * D)/H]) (bằng chữ: Q bằng căn bậc hai của [(2 nhân C nhân D) chia H].
Với giá trị cố định của C là 50, H là 30.
D lần lượt là 100,150,180
"""
import math

C = 50
H = 30
D = "100,150,180"
D = D.split(",")
value = []
for i in D:
    Q = str(round(math.sqrt((2 * C * int(i)) / H)))
    value.append(Q)
print(','.join(value))
