class Circle():
    def __init__(self, r):
        self.r = r
    def tinhBK(self):
        return self.r**2 * 3.14
c = Circle(2)
print(c.tinhBK())