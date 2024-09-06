# scores = [
#     [75, 83, 90],
#     [86, 86, 73],
#     [76, 95, 83],
#     [89, 96, 69],
#     [89, 76, 93],
#     [91, 70, 69, 2],
# ]
#
# for i in range(len(scores)):
#     for j in range(len(scores[i])):
#         score = scores[i][j]
#         print(score,end="\t")
#     print()

strings = [
    ['잠자리', '풍뎅이', '여치'],
    ['짜장면', '파스타', '피자', '국수']
]

for i in range(len(strings)):
    for j in range(len(strings[i])):
        print(strings[i][j])
    print()