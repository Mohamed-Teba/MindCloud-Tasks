class Garage:
    def __init__(self, capacity):
        self.__capacity = capacity          
        self.__available_spots = capacity   
        self.__cars = []                    

    def add_car(self, car_name):
        if self.__available_spots > 0:
            self.__cars.append(car_name)
            self.__available_spots -= 1
            print(f"{car_name} added to garage.")
        else:
            print("Garage is full!")

    def remove_car(self, car_name):
        if car_name in self.__cars:
            self.__cars.remove(car_name)
            self.__available_spots += 1
            print(f"{car_name} removed from garage.")
        else:
            print(f"{car_name} not found in garage.")

    def park_car(self, car_name):
        self.add_car(car_name)

    def display_available_spots(self):
        print(f"Available spots: {self.__available_spots} / {self.__capacity}")

g = Garage(3)
g.add_car("Toyota")
g.add_car("Honda")
g.display_available_spots()
g.remove_car("Toyota")
g.display_available_spots()