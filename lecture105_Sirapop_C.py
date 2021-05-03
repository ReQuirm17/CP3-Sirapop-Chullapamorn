class Vehicle:
    licenseNumber = ""
    serialCode = ""
    face = ""

    def turnOnAirConditioner(self):
        print("Turn On : Air")

class Car(Vehicle):
    pass

class PickUp(Vehicle):
    pass

class Van(Vehicle):
    pass

class Estatecar(Vehicle):
    pass

car1 = Car()
PickUp1 = PickUp()
Van1 = Van()
Estatecar1 = Estatecar()

car1.turnOnAirConditioner()
PickUp1.turnOnAirConditioner()
Van1.turnOnAirConditioner()
Estatecar1.turnOnAirConditioner()