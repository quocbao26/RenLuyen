"""
Định nghĩa một lớp gồm có tham số lớp và có cùng tham số instance
"""
class Person:

    name = "Person"

    def __init__(self, name):
        self.name = name

    @property
    def getName(self):
        return self.name

bao = Person("Bao")
print(bao.getName)

# an = Person()
# an.name = "Nico"
# an.old = 15
# print(an.name)
# print(an.old)