class Employee:
    def __init__(self, name, salary, role):
        self.name = name
        self.salary = salary
        self.role = role
    no_of_leave = 8
    def printDetails(self):
        return f"Name is {self.name}. Salary is {self.salary} and role is {self.role}"

    @classmethod
    def change_leaves(cls, newleaves):
        cls.no_of_leave = newleaves

    @staticmethod
    def printGood(string):
        print("This is a good " +string)

class Programmer(Employee):   # INHERIT
    def __init__(self, name, salary, role, language):
        self.name = name
        self.salary = salary
        self.role = role
        self.language = language


    def printProgrammer(self):
        return f" The programmer name is {self.name}. salary is {self.salary} and role is {self.role} & language id {self.language}"
    pass

biddut = Employee("Biddut", 550, "instructor")
bappi = Employee("Bappit", 560, "student")

badhon = Programmer("Badhon", 550, "Prorgrammer", ["python"])
Toha = Programmer("Toha", 770, "Prorgrammer", ["CPP"])

print(badhon.printProgrammer())
print(badhon.printDetails())


