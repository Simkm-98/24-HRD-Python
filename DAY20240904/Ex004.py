# x = int(input("점수를 입력해 주세요"))
# if x >= 80 :
#     print(f"{x} 점 합격입니다")
# elif x < 80 :
#     print(f"{x} 점 불합격입니다")
from copyreg import pickle

# age = int(input("나이를 입력해 주세요"))
# if age >= 65 :
#     print(f"{age}세는 입장이 무료입니다")
# else :
#     print("입장료를 내주세요")

resNum = input("주민번호를 입력해 주세요 : ")

if len(resNum) == 14 and resNum[6] == '-':  # 올바른 형식인지 확인
    if resNum[7] in '13':
        print("남성입니다.")
    elif resNum[7] in '24':
        print("여성입니다.")
    else:
        print("올바른 주민번호가 아닙니다.")
else:
    print("주민번호 형식이 올바르지 않습니다.")

passWord = input("비밀번호를 입력해 주세요 : ")

if passWord == "123456" :
    print("Login Success")
else :
    print("Login Failed")