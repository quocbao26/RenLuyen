"""
Bạn hãy viết một chương trình để in thời gian thực thi (running time of execution) phép tính "1+1" 100 lần.
Gợi ý:
Sử dụng timeit() để đo thời gian chạy
"""
from timeit import Timer
t = Timer("for i in range(100):1+1")
print (t.timeit())
#Khi chạy code trên, bạn cần phải đợi để phép tính trên được thực hiện xong
# rồi chương trình mới in ra thời gian thực thi.
# Ban đầu khi mới chạy code, cảm giác như không có gì đang được thực thi.