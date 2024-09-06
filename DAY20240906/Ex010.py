# subject = ['국어', '수학', '영어', '과학', '사회']
# score = []
# sum: int = 0
# for sub in subject:
#     subIn = input(f"{sub} 점수를 입력해 주세요( -1 입력 시 종료) : ")
#
#     if subIn == -1:
#         break
#     else:
#         score.append(subIn)
#         sum += int(subIn)
#
# for i in range(len(subject)):
#     print(f'{subject[i]} 점수는 {score[i]}', end=", ")
# print()
# print(f"총 합은 : {sum}, 평균 점수는 : {sum/len(subject)}")

numbers = [
    [10, 20, 30],
    [40, 50, 60, 70, 80]
]

for row1 in numbers:
    for element1 in row1:
        print(element1, end=" ")
    print()

sum1 = 0

for row1 in numbers:
    for element1 in row1:
        sum1 += element1

print(sum1)

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# 모든 요소 출력
for row in matrix:
    for element in row:
        print(element, end=" ")
    print()  # 줄 바꿈

# 모든 요소의 합 계산
total = 0
for row in matrix:
    for element in row:
        total += element

print(f"모든 요소의 합: {total}")

# 각 행의 합 계산
for i, row in enumerate(matrix):
    row_sum = sum(row)
    print(f"{i+1}번째 행의 합: {row_sum}")