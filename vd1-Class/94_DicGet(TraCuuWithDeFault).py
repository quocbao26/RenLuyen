"""
Viết chương trình đếm và in số ký tự của chuỗi do người dùng nhập vào.
Ví dụ:
Nếu chuỗi nhập vào là quantrimang.com thì đầu ra sẽ là:
q,1
u,1
a,2....
"""
#Cách 1
def countStr(s):
    dic = {}
    for i in s:
        if i == " ":
            continue
        else:
            dem = s.count(i)
            dic[i] = dem
    return dic
s = 'quantrima ng.com'
dic = countStr(s)
for k,v in dic.items():
    print(k, "-", v )

#Cách 2
#Sử dụng dict.get() để tra cứu key với giá trị mặc định.
s = 'quantrima ng.com'
dic = {}
for c in s:
 dic[c] = dic.get(c,0)+1
print ('\n'.join(['%s,%s' % (k, v) for k, v in dic.items()]))