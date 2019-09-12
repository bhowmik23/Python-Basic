class Employee:
    def __init__(self, fName, lName):
        self.fName= fName
        self.lName= lName
        # self.email = f"{fName}.{lName}@gmail.com"

    def explain(self):
        return f" This emlpoyee is {self.fName} {self.lName}"
    @property
    def Email(self):
        if self.fName==None or self.lName==None:
            return "Email is not set"
        else:
           return f"{self.fName}.{self.lName}@gmail.com"


    @Email.setter
    def Email(self, string):
        print("Setting now")
        names = string.split("@") [0]
        self.fName = names.split(".")[0]
        self.lName = names.split(".") [1]

    @Email.deleter
    def Email(self):
        self.fName = None
        self.lName = None

biddut = Employee("Biddut", "Bhowmik")
o = "This is a string"
# print(biddut.Email)
# print(id(biddut))
# print(dir(biddut))
# print(type(biddut))

import inspect
print(inspect.getmembers(biddut))
