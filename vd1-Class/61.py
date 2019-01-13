"""
In chuỗi Unicode "Hello world".
"""
s = u'Hello world'
print(s)

#Viết chương trình để đọc chuỗi ASCII và chuyển đổi nó sang một chuỗi Unicode được mã hóa bằng UTF-8.
#Gợi ý:
#Sử dụng hàm encode() để chuyển đổi.
print(s.encode(encoding='utf-8'))