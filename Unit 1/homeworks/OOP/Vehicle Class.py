class Vehicle:
    def __init__(self , Maxspeed , Mileage):
        self.Maxspeed = Maxspeed
        self.Mileage = Mileage
Vehicle_model = input("please input your vehicle model: ")
Maxspeed = input("Please enter the cars' max speed: ")
Mileage = input("please enter the cars' mileage: ")
Vehicle_model = str(Vehicle_model)
Maxspeed = int(Maxspeed)
Mileage = int(Mileage)

Vehicle_model = Vehicle(Maxspeed, Mileage)

print(Vehicle_model.Maxspeed,Vehicle_model.Mileage)

#and now to the child class bus (part4 of the homework)
class Bus(Vehicle):
    pass

