class A:
    def __init__(self):
        self.s = ""
    def getString(self):
        self.s = input("Nhập chuỗi:")
    def printString(self):
        print(self.s)
s = A()
s.getString()
s.printString()

