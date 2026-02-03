from random import randint
class Train:
    def __init__(self,name,ticket,status):
        self.name=name
        self.ticket=ticket
        self.status=status
        # self.fare=fare
    def getInfo(self):
        print(f"The passanger name is {self.name}.")
        print(f"The ticket is {self.ticket}, the status is {self.status}")
        print(f"The price of ticket is {randint(399,1200)}.")

ayush=Train("Ayush","booked","running")
dakesh=Train("Dakesh kothe","RAC","At 30/7/2025")
ayush.getInfo()
print("thank u for visiting site")
print(" ")
dakesh.getInfo()
print("thank u for visiting site")