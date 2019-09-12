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


bangaliSuporter = Employee("Bangali", "Suporter")
# biddut = Employee("Biddut", "Bhowmik")
print(bangaliSuporter.Email)
# print(bangaliSuporter.Email())

bangaliSuporter.fName= "Us"
print(bangaliSuporter.Email)
# print(bangaliSuporter.Email())

bangaliSuporter.Email= "this.that@gmail.com"
print(bangaliSuporter.fName)
print(bangaliSuporter.lName)
print(bangaliSuporter.Email)

del bangaliSuporter.Email
print(bangaliSuporter.Email)