# 1. 더하기
# 2. 뺴기
# 3. 곱하기
# 4. 나누기
#
# 계산기 기능 선택

stop = True

print("기능을 선택하세요")
print(" 1. 더하기 ")
print(" 2. 빼기 ")
print(" 3. 곱하기 ")
print(" 4. 나누기 ")

while stop:
    select = input("계산기 기능을 선택하세요 (1, 2, 3, 4, 종료:q): ")
    if select == "q":
        print("종료합니다")
        stop = False
    elif select in ["1", "2", "3", "4"]:
        num1 = int(input("첫번째 정수를 입력하세요: "))
        num2 = int(input("두번째 정수를 입력하세요: "))
        if select == "1":
            print(f"{num1} + {num2} = {num1 + num2} 입니다")
        elif select == "2":
            print(f"{num1} - {num2} = {num1 - num2} 입니다")
        elif select == "3":
            print(f"{num1} * {num2} = {num1 * num2} 입니다")
        elif select == "4":
            if num2 != 0:
                print(f"{num1} / {num2} = {num1 / num2} 입니다")
            else:
                print("0으로 나눌 수 없습니다.")
    else:
        print("(1, 2, 3, 4, q) 중 선택해 주세요")