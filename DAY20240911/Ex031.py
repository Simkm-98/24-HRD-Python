import math
# 소수점 절삭처리

print('3.6의 소수점 절삭(버림) : %.1f' % math.floor(3.6))
print('5.1의 무조건 올림 : %.1f' % math.ceil(5.1))
print('6.3의 반올림 : %.1f' % round(6.3))
print('6.6의 반올림 : %.1f' % round(6.6))
# 펙토리알 구하기
print('5의 펙토리알(1*2*3*4*5) : %d' % math.factorial(5))

# 삼각함수
print('sin(pi/4) : %.2f' % math.sin(math.pi/4))
print('cos(pi) : %.2f' % math.cos(math.pi))
print('tan(pi/6) : %.2f' % math.tan(math.pi/6))

# 거듭제곱, 제곱근, 로그 구하기
print('5의 3승 : %d' % math.pow(5,3))
print('144의 제곱근 : %d' % math.sqrt(144))
print('log10(1000) : %.2f' % math.log10(1000))
