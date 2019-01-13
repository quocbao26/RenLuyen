"""
Viết một chương trình để tạo tất cả các câu có chủ ngữ nằm trong ["Anh","Em"],
động từ nằm trong ["Chơi","Yêu"] và tân ngữ là ["Bóng đá","Xếp hình"].
"""
chu_ngu = ["Anh","Em"]
dong_tu = ["Chơi","Yêu"]
tan_ngu = ["Bóng đá","Xếp hình"]
#Cach 1
# for i in range(len(chu_ngu)):
#     for j in range(len(dong_tu)):
#         for k in range(len(tan_ngu)):
#             cau = "%s %s %s" % (chu_ngu[i], dong_tu[j], tan_ngu[k])
#             print(cau)
#Cach 2
for i in chu_ngu:
    for j in dong_tu:
        for k in tan_ngu:
            cau = "%s %s %s" % (i,j,k)
            print(cau)