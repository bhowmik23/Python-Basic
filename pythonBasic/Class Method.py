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

    @classmethod
    def from_dash(cls, string):
        # params = string.split("-")
        # print(params)
        # return cls(params[0], params[1], params[2])
        return cls(*string.split("-"))
    @staticmethod
    def printGood(string):
        print("This is a good " +string)
        return "anything"



biddut = Employee("Biddut", 550, "instructor")
bappi = Employee("Bappit", 560, "student")
badhon = Employee.from_dash("karan-480-student")


# biddut.name= "Biddut"
# biddut.salary= 550
# biddut.role= "Student"
#
# bappi.name= "Bappi"
# bappi.salary= 549
# bappi.role= "Student"

# Employee.no_of_leave = 89
print(badhon.salary)
biddut.change_leaves(34)
print(biddut.no_of_leave)
print(bappi.printDetails())
print(badhon.printGood("Biddut"))