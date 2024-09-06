# menu = ('짜장면', '우동', '짬뽕', '볶음밥')
#
# print(menu)
# print(menu[0])
# print(menu[1])
# print(menu[0:3])
# # menu[1] = '사천탕면' # 수정불가
#
# tup1 = (10, 20, 30)
# tup2 = (40, 50, 60)
# tup3 = tup1 + tup2 # 새롭게 tup3 튜플이 생성됨
# print(tup3)

dans = (2, 3, 4, 5, 6, 7, 8, 9)
print('구구단표')
print('=' * 50)
for dan in dans :
    print(str(dan) + '단')
    for i in range(1, 10) :
        print('%d x %d = %d' % (dan, i, dan*i))
    print('-' * 30)

admin = ('rubato', '12345', 'rubato@naver.com')
print('- 관리자 정보')
print('아이디 : ' + admin[0])
print('비밀번호 : ' + admin[1])
print('이메일 : ' + admin[2])
