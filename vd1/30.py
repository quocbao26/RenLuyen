"""
Định nghĩa một hàm có input là 2 chuỗi và in chuỗi có độ dài lớn hơn trong giao diện điều khiển.
Nếu 2 chuỗi có chiều dài như nhau thì in tất cả các chuỗi theo dòng.
"""
def inchuoi(s, s1):
    if len(s) > len(s1):
        print(s)
    elif len(s) < len(s1):
        print(s1)
    else:
        print(s)
        print(s1)
inchuoi("one", "thr")