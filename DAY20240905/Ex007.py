# for _ in range(5):
#     print("안녕하세요")
# for x in "안녕하세요" :
#     print(f"{x} : 안녕하세요.")
# print("#" * 40)
# for x in ['안','녕하','세', 0] :
#     print("안녕하세요.")
#
# sum = 0
# for i in [1, 2, 3, 4, 5,6, 7, 8, 9, 10] :
#     sum += i
#     print(f"값 : {sum}")
# for i in range(10) :
#     print(i, end="")
# print("\n")
# print("#" * 40)
# sum = 0;
# for i in range(0, 201, 5) :
#     print(i, end=" ")
#     sum += i
# print(sum)
# print("#" * 40)
# for i in range(100, 301):
#     if i % 3 == 0:
#         print(f"3의 배수 : {i}", end=" ")
#
# x: str = input("영어 입력 : ")
# for i in x:
#     print(i, end=" ")
#
# for a in range(1, 10) :
#     print("\n")
#     for b in range(1,10) :
#         print(f"{a} * {b} = {a * b},", end=" ")
#
# i = 1
# sum = 0
# while i <= 100 :
#     sum += i
#     i += i
#     print(f"i : {i}, sum : {sum}")
#
# print(f"총합 : {sum}")

s = 'Python is widely used by a number of big companies'
s = s.lower()
size = len(s)
i = 0
count = 0
print('모음 : ', end="")
while i < size :

    if (s[i] == 'a' or
            s[i] == 'e' or
            s[i] == 'i' or
            s[i] == 'o'or
            s[i] == 'u') :
        count += 1
        print(f'{s[i]},', end=" ")
    i += 1
print('\n')
print(f"모음의 개수 : {count}")