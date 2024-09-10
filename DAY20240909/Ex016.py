def cir_area(radius) :
    area = radius * radius * 3.14
    return area

def cir_circum(radius) :
    circum = 2 * 3.14 * radius
    return circum

def cir_volume(r, height) :
    volume = r * height
    return volume
r = float(input('반지름을 입력하세요: '))
h = float(input('높이를 입력하세요: '))
a = cir_area(r)
b = cir_circum(r)
c = cir_volume(a, h)
print('원의 면적 : %.2f, 원주의 길이 :%.2f, 원기둥의 부피 : %2.f' % (a, b, c))