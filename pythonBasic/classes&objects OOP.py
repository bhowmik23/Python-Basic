# Classes - Templete
# Object - Instance of the class

# DRY - DO not repeat Yourself

# class Student:
#     pass
# biddut = student()
# bappi = student()
#
# biddut.name= "Biddut"
# biddut.SID = 12
# biddut.section ="B"
# biddut.subjects = ["Bangla", "English", "Physics", "ICT"]
# print(biddut.name, biddut.subjects[0])

'''class Employee:
    no_of_leaves = 8
    pass
biddut= Employee()
bappi = Employee()

biddut.Name = "Biddut"
biddut.Salary = 550
biddut.Role = "Instructor"

bappi.Name = "Biddut"
bappi.Salary = 55056
bappi.Role = "Instructor"
print(biddut.no_of_leaves, biddut.Salary)
print(biddut.__dict__)
Employee.no_of_leaves = 9
print(Employee.no_of_leaves)'''

'''class Robot:
    # def __init__(self, givenName, givenColor, givenWeight):
    #     self.name=givenName
    #     self.color=givenColor
    #     self.weight=givenWeight
    def __init__(self, name, color, weight):
        self.name=name
        self.color=color
        self.weight=weight
    def introduce_self(self):
        print("My name is: " +self.name)

# r1= Robot()
# r1.name= "Tom"
# r1.color= "Red"
# r1.weight= 30
# r2= Robot()
# r2.name= "Jerry"
# r2.color= "Gray"
# r2.weight= 5

r1 = Robot("Tom", "Red",20)
r2 = Robot("Jerry", "Blue",5)

r1.introduce_self()
r2.introduce_self()

class Person:
    def __init__(self, n, p, i):
        self.name = n
        self.personality = p
        self.is_sitting = i

    def sit_dpwn(self):
        self.is_sitting=True
    def stand_uo(self):
        self.is_sitting = False

p1 = Person("Alice", "aggressive", False)
p2 = Person("Becky", "talktive", True)
p1.robot_owned = r2
p2.robot_owned = r1
p1.robot_owned.introduce_self()'''



class Employee:
    def __init__(self, name, salary, role):
        self.name = name
        self.salary = salary
        self.role = role
    no_of_leave = 8
    def printDetails(self):
        return f"Name is {self.name}. Salary is {self.salary} and role is {self.role}"

biddut = Employee("Biddut", 550, "instructor")
bappi = Employee("Bappit", 560, "student")


# biddut.name= "Biddut"
# biddut.salary= 550
# biddut.role= "Student"
#
# bappi.name= "Bappi"
# bappi.salary= 549
# bappi.role= "Student"

print(biddut.printDetails())
print(bappi.printDetails())






