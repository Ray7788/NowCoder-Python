class Employee:
    def __init__(self, name, salary,):
        self.name = name
        self.salary = salary
        # self.age = age
    
    def printclass(self):
        try:
            print(f"{self.name}'salary is {self.salary}, and his age is {self.age}")
        except:
            print("Error! No age")

            
name = input()
salary = int(input())

e = Employee(name,salary)
e.printclass()

e.age = int(input())
e.printclass()
