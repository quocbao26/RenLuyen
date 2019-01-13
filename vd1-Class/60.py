"""
Viết một chương trình chấp nhận chuỗi từ được phân tách bằng khoảng trống và in các từ chỉ gồm chữ số.

Ví du: Nếu những từ sau đây là đầu vào của chương trình: 3 quantrimang.com và 2 python. Đầu ra sẽ là ['3', '2']
"""
import re
s = "3 quantrimang.com và 2 python 3"
print(re.findall(r'\d+',s))