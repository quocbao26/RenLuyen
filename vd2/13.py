"""
Viết một chương trình chấp nhận đầu vào là một chuỗi các từ tách biệt bởi khoảng trắng,
 loại bỏ các từ trùng lặp, sắp xếp theo thứ tự bảng chữ cái, rồi in chúng.

Giả sử đầu vào là: hello world and practice makes perfect and hello world again
Thì đầu ra là: again and hello makes perfect practice world
"""
chuoi = "hello world and practice makes perfect and hello world again"

words = [word for word in chuoi.split(" ")]
print(" ".join(sorted(list(set(words)))))

