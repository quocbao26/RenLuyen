class Shape():
    def __init__(self, cd):
        self.cd = cd
    def area(self):
        return self.cd
class Square(Shape):
    def __init__(self,cd):
        Shape.__init__(self, cd)
        self.cd = cd
    def area(self):
        return self.cd * self.cd
sa = Square(3)
print(sa.area())
