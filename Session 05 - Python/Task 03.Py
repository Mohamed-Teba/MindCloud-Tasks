class Car:
    def __init__(self, name):
        self.name = name

    def drive(self):
        print("Driving the car")

    def show_info(self):
        print(f"Car name/brand: {self.name}")


class Battery:
    def charge(self):
        print("Battery is charging")

    def check_range(self, current_charge):
        remaining = current_charge * 5
        print(f"Estimated remaining range: {remaining} km")


class ElectricCar(Car, Battery):
    def __init__(self, name):
        Car.__init__(self, name)


ec = ElectricCar("Tesla Model 3")
ec.show_info()
ec.drive()
ec.charge()
ec.check_range(80)