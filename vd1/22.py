from operator import itemgetter, attrgetter
# Bài tập Python 22 Code by Quantrimang.com
l = []
while True:
    s = input()
    if not s:
       break
    l.append(tuple(s.split(",")))

print(sorted(l, key=itemgetter(1, 0, 2)))