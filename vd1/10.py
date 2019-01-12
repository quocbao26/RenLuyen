"""
Viết một chương trình có 2 chữ số, X, Y nhận giá trị từ đầu vào và tạo ra một mảng 2 chiều.
Giá trị phần tử trong hàng thứ i và cột thứ j của mảng phải là i*j.

Lưu ý: i=0,1,...,X-1; j=0,1,...,Y-1.

Ví dụ: Giá trị X, Y nhập vào là 3,5 thì đầu ra là: [[0, 0, 0, 0, 0], [0, 1, 2, 3, 4], [0, 2, 4, 6, 8]]
"""
x = int(input("Nhập x: "))
y = int(input("Nhập y: "))
mul = [[0 for col in range(y)] for row in range(x)]

for i in range(x):
    for j in range(y):
        mul[i][j] = i * j
print(mul)




