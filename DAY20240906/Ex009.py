# question = ['tr_in', 'b_s', '_axi', 'air_lane']
# answers = ['a', 'u', 't', 'p']

# for i in range(len(question)):
#     q = '%s 에서 밑줄(_) 안에 들어갈 알파벳은? ' % question[i]
#     ans = input(q)
#
#     if ans == answers[i]:
#         print("정답입니다!")
#     else:
#         print("틀렸습니다")
# count_1= 0
# count_2= 0
# for i in question:
#     q = '%s 에서 밑줄(_) 안에 들어갈 알파벳은? ' % i
#     ans = input(q)
#     if ans == answers[question.index(i)]:
#         print('정답입니다.')
#         count_1 += 1
#     else:
#         print("틀렸습니다")
#         count_2 += 1
#
# print(f'정답 : {count_1}개, 오답 : {count_2}개')

flowers = ['할미꽃', '무궁화', '장미', 'Iris',]
flowers.append('국화')
print(flowers)
flower = ['물망초']
new_flower = flowers + flower
print(new_flower)