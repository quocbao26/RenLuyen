"""
Xác định một class với generator có thể lặp lại các số nằm trong khoảng 0 và n, và chia hết cho 7.
"""

def putnumbers(n):
    i = 0
    while i < n:
        j = i
        i += 1
        if j % 7 == 0:
            yield j
for i in putnumbers(100):
    print(i)