# class Fruit :
#     name = '오렌지'
#     color = '노란색'
#     def taste(self) :
#         print('새콤하다.')
#     def vitamin(self):
#         print('비타민 C가 풍부하다.')
#
# orange = Fruit()
# print('과일명 : %s' % orange.name )
# print('색상 : %s' % orange.color)
# orange.taste()
# orange.vitamin()

class Student:
    name = ""
    student_id = 0
    department = ""
    def __init__(self, name, student_id, department):
        self.name = name
        self.student_id = student_id
        self.department = department

stu = Student(department="HRD", name="경민", student_id=8)
print(stu.name)
print(stu.student_id)
print(stu.department)
print(stu)