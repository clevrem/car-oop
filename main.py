class Car:
    def __init__(self,fuel_level,volume=70):
        if fuel_level>volume:
            raise ValueError("bu sig'maydi")
        self.volume=volume
        self.fuel_level=fuel_level

    def drive(self, distance):
        need_fuel=distance/10
        if self.fuel_level >= need_fuel:
            print(f"bu {distance} km yurdi")
            self.fuel_level-= need_fuel
        else:
            print("yonilg'i oz !")
    def refuel(self,amount):
        if self.fuel_level +amount > self.volume:
            print(" buncha yonilg'i sigmaydi !!!")
        self.fuel_level +=amount




car1=Car(32)
car1.drive(100)
car1.drive(2)
car1.refuel(10)
car1.drive(5)