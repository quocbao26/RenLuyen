class Vietnam(object):
    def __init__(self, status):
        self.__status = status
    def printNaotionality1(self):
        print(self.__status)


class Hanoi(Vietnam):
    def __init__(self,status):
        super(Hanoi, self).__init__(status)

    def printNaotionality(self):
        print("Hanoi")

hn = Hanoi("Bảo")
hn.printNaotionality1()