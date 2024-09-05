score = int(input("점수를 입력하세요 : "))
result:str = ''
if score >= 90 :
    result = 'A'
elif score >= 80 :
    result = 'B'
elif score >= 70 :
    result = 'C'
elif score >= 60 :
    result = 'D'
else :
    result = 'F'

print(f"당신의 성적은  '{result} 입니다")