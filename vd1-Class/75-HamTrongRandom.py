"""
Viết chương trình xuất ra một số chẵn ngẫu nhiên trong khoảng 0 đến 10 (bao gồm cả 0 và 10),
sử dụng module random và list comprehension.

Gợi ý:

Sử dụng random.choice() để tạo một phần tử ngẫu nhiên từ list.
"""
import random
lst = [x for x in range(0,11) if x % 2 == 0]
print(random.choice(lst))

#Vui lòng viết chương trình để xuất một số ngẫu nhiên,
# chia hết cho 5 và 7, từ 0 đến 200 (gồm cả 0 và 200), sử dụng module random và list comprehension.
lst = [x for x in range(0,201) if x % 5 == 0 and x % 7 == 0]
print(random.choice(lst)) # choice: chọn 1 số ngẫu nhiên từ list

#Vui lòng viết chương trình để tạo một list với 5 số ngẫu nhiên từ 100 đến 200.
#Sử dụng random.sample() để tạo list chứa các giá trị ngẫu nhiên.
lst = random.sample(range(100,201),1)
print(lst)

#Vui lòng viết chương trình để tạo một list với 5 số chẵn từ 100 đến 200.
print(random.sample([x for x in range(100,201) if x % 2 == 0],5))

#Viết chương trình để tạo ngẫu nhiên một list gồm 5 số, chia hết cho 5 và 7, nằm trong đoạn [1;1000].
print(random.sample([x for x in range(1,1001) if x % 5 == 0 and x % 7 == 0],5))

#Viết chương trình để in một số nguyên ngẫu nhiên từ 7 đến 15.
for i in range(1,11):
    print(random.randrange(7,16), end=",")
    