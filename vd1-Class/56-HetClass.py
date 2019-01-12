"""
Viết hàm để tính 5/0 và sử dụng try/exception để bắt lỗi.
"""
try:
    print(5/0)
except ZeroDivisionError as erorr:
    print("Lỗi chia 0:",erorr)
except Exception as problem:
    print ('Bắt được một exception')
finally:
    print ('Phép tính bị hủy')