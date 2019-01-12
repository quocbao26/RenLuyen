netamount = 0
while True:
    s = input("Nhật ký giao dịch: ")
    if not s:
        break
    values = s.strip().split(' ')
    for i in range(len(values)//2):
        amount = int(values.pop())
        operation = values.pop()


        if operation == "D":
            netamount += amount
        elif operation == "W":
            netamount -= amount
        else:
            pass
    print("Tiền còn lại:", netamount)



