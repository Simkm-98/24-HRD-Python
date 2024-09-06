# p.228 ex
# numbers = [1, 1, 2, 3, 4, 2, 3, 4, 5, 1, 2, 3, 6, 6, 5, 6, 7, 8, 8, 8, 9, 1, 9]
# counter = {}
#
# for number in numbers:
#     count = 0
#     for num in numbers:
#         if num == number:
#             count += 1
#     if number not in counter or count > counter[number]:
#         counter[number] = count
#
# # p. 229 ex
character = {
    "name" : "기사",
    "level" : 12,
    "items" : {
        "sword": "불꽃의 검",
        "armor": "풀플레이트"
    },
    "skill": ["베기", "세게 베기", "아주 세게 베기"]
}


for key in character:
    if type(character[key]) is dict:
        for item_key, item_value in character[key].items():
            print(f"{item_key} : {item_value}")
    elif type(character[key]) is list:
        for item in character[key]:
            print(f"{key} : {item}")
    else:
        print(f"{key} : {character[key]}")

# V = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# value1 = V[0][0] # get = read
# # print(value1)
# # value2 = V[0] # scalar
# # print(value2) # 리스트 타입(즉, 벡터타입)
#
# for i in range(0, 3):
#     for j in range(0, 3):
#         scalar = V[i][j]
#         print(scalar, end="\t")
#     print()

# animals: list = ['사자', '토끼', '하이애나', '기린']
# index = 0
# size = len(animals)
# print(animals)
# for ani in animals:
#     print(ani, end=", ")
# while index < size:
#     animal: str = animals[index]
#     print(animal, end=", ")
#     index += 1

# a=[1, 2, 3]
# b=['4', 5, 6, 7]
# c = a + b
# print(len(c))