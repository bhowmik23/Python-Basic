# class Dad:
#     basketball = 1
# class Son(Dad):
#     dance = 1
#     def idDance(self):
#         return f" Yes I dance {self.dance} no of time"
# class Grandson(Son):
#     dance = 6
#
#     def idDance(self):
#         return f" Yes I dance awesomely {self.dance} no of time"
#
# Darry = Dad()
# Larry = Son()
# harry = Grandson()
#
# print(harry.idDance())
# print(harry.basketball)

class ElectrinicDevie:
    quantity = 9
    def printElectronicDeviceDetails(self):
        return f"No of Electronic Device: {self.quantity}"
class PocketGadget(ElectrinicDevie):
    quantity = 8
    def printPocketDeviceDetails(self):
        return f"No of Pocket Gadget: {self.quantity}"

class Phone(PocketGadget):
    quantity = 50

    def printPhoneDetails(self):
        return f"No of Pocket Device: {self.quantity}"

electronicDevice = ElectrinicDevie()
pocketGadget = PocketGadget()
Phone = Phone()

print(electronicDevice.printElectronicDeviceDetails())