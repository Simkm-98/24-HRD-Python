# scores = {
#     '김채린': 85,
#     '박수정': 98,
#     '함소희': 94,
#     '안예린': 90,
#     '연수진': 93
# }
#
# sum = 0
# for key in scores :
#     sum += scores[key]
#     print('%s : %d' % (key , scores[key]))
#
# avg = sum/len(scores)
# print('합계 : %d, 평균 : %.2f' % (sum, avg))
# print(scores)
# phones = {
#     '삼성 갤럭시' : {
#         '갤럭시 S5': 2014,
#         '갤럭시 S7': 2016,
#         '갤럭시 노트8': 2017,
#         '갤럭시 S9': 2018
#     },
#     '애플 아이폰' : {
#         '아이폰 5' : 2014,
#         '아이폰 7' : 2016,
#         '아이폰 9' : 2017,
#         '아이폰 10' : 2018
#     }
# }
# print(phones)
# for key in phones :
#     for item_key, item_value in phones[key].items():
#         print(f"{item_key} : {item_value}")
#
# print(len(phones))