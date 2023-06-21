class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def printclass(self):
        print(f"{self.name}'salary is {self.salary}, and his age is {self.age}")


name = input()
salary = input()

e = Employee(name, salary)

if hasattr(e, "age"):
    e.printclass()
if hasattr(e, "age") is False:
    print(hasattr(e, "age"))
    e.age = input()
    e.printclass()
