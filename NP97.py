class Student:
    def __init__(self, name, num, mark, grade):
        self.name = name
        self.num = num
        self.mark = mark
        self.grade = grade

    def prints(self):
        print(
            f"{self.name}'s student number is {self.num}, and his grade is {self.mark}. He submitted {len(self.grade)} assignments, each with a grade of {' '.join(self.grade)}"
        )

name = input()
num = input()
mark = int(input())
grade = input().split()
stu = Student(name, num, mark, grade).prints()
