file = open(file="score.txt", encoding="UTF-8", mode="r")

for line in file:
    print(line.strip())  # 각 줄의 원본 내용 출력
    values = line.split()
    if len(values) == 6:  # 이름과 5개의 점수가 있는지 확인
        name = values[0]
        scores = [int(score) for score in values[1:]]
        total = sum(scores)
        print(f"{name}의 TOTAL score : {total}")
        print(f"{name}의 평균 : {total/5}\n")

file.close()