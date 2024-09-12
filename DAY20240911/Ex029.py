class Student :
    total = 0
    avg = 0.0

    def __init__(self, name, kor, eng, math) :
        self.name = name
        self.kor = kor
        self.eng = eng
        self.math= math

    def getSum(self) :
        self.total = self.kor + self.eng + self.math
        return self.total

    def getAvg(self) :
        self.avg = self.total /3
        return self.avg

s1 = Student('심경민', 90, 90, 100)
print('이름 : %s' % s1.name)
print('합계 : %d' % s1.getSum())
print('평균 : %.1f' % s1.getAvg())