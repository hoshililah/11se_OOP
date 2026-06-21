#---begin Python ---
class Car:
    def __init__(self, make, model, year, colour):
        self.make = make
        self.model = model
        self.__year = year
        self.colour = colour

    # Getter method to retrieve the value of the private attribute
    def get_year(self):
        return self.__year

    # Setter method to modify the value of the private attribute 
    def set_year(self, value):
        self.__year = value

    def start(self):
        print(f"{self.make} {self.model} is starting.")

    def stop(self):
        print(f"{self.make} {self.model} is stopping.")

class ElectricCar(Car):
    def start(self):
        print(f"{self.make} {self.model} is starting silently.")

electric_car = ElectricCar("Tesla", "Model S", 2022, "White")
electric_car.start() 

# Instantiating objects from the Car class
car1 = Car("Toyota", "Camry", 2020, "Red")
car2 = Car("Honda", "Civic", 2018, "Blue")
car3 = Car("Ford","Mustang",2021,"Black")

car1.set_year(2021)
print(car1.get_year()) 

car1.start()  # Output: Toyota Camry is starting.
car2.stop()   # Output: Honda Civic is stopping.
car3.start()  # Output: Ford Mustang is starting.
#--- end python ---

