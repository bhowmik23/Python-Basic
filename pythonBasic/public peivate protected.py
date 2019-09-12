# Public - public   no underscore use
# Private -  __private double underscore (only that class use is)
# Protected - _protected  single underscore (only subclasses use)
class Employee:
    no_of_leaves = 8
    var =8
    _procted = 9
    __private = 98
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
class Player:
    var = 9
    no_of_games = 4
    def __init__(self, name, game):
        self.name= name
        self.game = game

    def printdetail(self):
        return f" The name is {self.name}. game is {self.game}"

class coolProgrammer(Employee, Player):
    var = 10
    language = "C++"
    def printLanguage(self):
        print(self.language)

badhon = Programmer("Badhon", 550, "Prorgrammer", ["python"])
Toha = Programmer("Toha", 770, "Prorgrammer", ["CPP"])

shubham = Player("Shubham", ["Cricketer"])
karon = coolProgrammer("karan", 8999, "coolProgrammer")

print(badhon._procted)
print(badhon._Employee__private)