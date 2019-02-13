class Nguoi():
    def getGender(self):
        return "Trống"
class Nam(Nguoi):
    def getGender(self):
        return "Nam"
class Nu(Nguoi):
    def getGender(self):
        return "Nữ"
nam = Nam()
nu = Nu()
print(nam.getGender())
print(nu.getGender())