# class Animal(object):
#     name = "고양이" # property == instance 변수 # public
#     def sound(self):
#         print("야옹")
#
# cat = Animal()
# print(Animal.name)
# cat.sound()
#
# class Dog:
#     def __init__(self, name):
#         self.name = name  # 인스턴스 변수 설정
#
#     def bark(self):
#         print(f"{self.name}가 짖습니다: 왈왈!")
#
# my_dog = Dog("멍멍이")
# my_dog.bark()  # 출력: 멍멍이가 짖습니다: 왈왈!

class Animal:
    def __init__(self, name):
        self.name = name

    def sound(self):
        if self.name == "강아지" :
            print(f"{self.name} : 왈왈!!")
        elif self.name == "고양이":
            print(f"{self.name} : 야옹!!")
        else:
            print(f"{self.name} : ??")

dog = Animal("강아지")
cat = Animal("고양이")
animal = Animal("Animal")
dog.sound()
cat.sound()
animal.sound()