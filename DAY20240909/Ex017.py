#
# minimum = 0
# maximum = 0
#
# input_value1 = int(input("첫번째 입력 : "))
# input_value2 = int(input("두번째 입력 : "))
#
# def find_gcm(input_value1:int, input_value2:int) -> int:
#     if input_value1 > input_value2:
#         minimum = input_value2
#     else:
#         minimum = input_value1
#
#     gcm = 0
#
#     for number in range(2, minimum + 1):
#         if input_value1 % number == 0 and input_value2 % number == 0:
#             gcm = number
#
#     return gcm
#
# gcm = find_gcm(input_value1=input_value1, input_value2=input_value2)
# print(f"최대 공약수는 : {gcm}")
#
# def isPrimeNumber(a) :
#     prime_yes = True
#     for i in range(2, a) :
#         if a % i == 0 :
#             prime_yes = False
#             break
#     return prime_yes
#
# n = int(input("n 값을 입력해 주세요 : "))
#
# print('2 ~ %d까지의 정수 중 소수 :' % n, end = ' ')
# for a in range(2, n+1) :
#     is_prime = isPrimeNumber(a)
#     if is_prime :
#         print(a, end=' ')

def matchWord(in_word, answer):
    if in_word == answer :
        msg = '참 잘했어요~'
    else:
        msg = '단어 공부를 좀 해야겠어요~'
    return msg

eng_dict = {'apple':'사과', 'lion':'사자', 'book':'책', 'love':'사랑', 'friend':'친구'}

for i in eng_dict:
    string = input(eng_dict[i] + '에 맞는 영어단어는?')
    result = matchWord(string, i)
    print(result)