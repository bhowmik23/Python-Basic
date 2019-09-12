class Employee:
    no_of_leaves = 8

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

    def __add__(self, other):
        return self.salary+ other.salary

    def __truediv__(self, other):
        return  self.salary/other.salary

    def __repr__(self):
        # return self.printDetails()
        return f"Employee ('{self.name}', {self.salary}, '{self.role}')"
emp1 = Employee("biddut", 3565, "Programmer")
emp2 = Employee("bappi", 356, "cleaner")
print(emp1 + emp2)
print(emp1 / emp2)
print(repr(emp1))