"""
Viết chương trình để giải 1 câu đố cổ của Trung Quốc:
Một trang trại thỏ và gà có 35 đầu, 94 chân, hỏi số thỏ và gà là bao nhiêu?
"""
dau = 35
chan = 94
def giai(dau,chan):
    for i in range(dau+1):
        j = dau - i
        if 2 * i + 4 * j == chan:
            return i, j
        return "Khong do dap an"
print(giai(dau,chan))