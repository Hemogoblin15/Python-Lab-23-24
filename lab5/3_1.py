class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year


class Car(Vehicle):
    def __init__(self, make, model, year, capacity):
        super().__init__(make, model, year)
        self.capacity = capacity

    def calculate_mileage(self):
        self.mileage = 2 * self.capacity

    def calculate_towing_capacity(self):
        self.towing_capacity = 2 * self.capacity


class Motorcycle(Vehicle):
    def __init__(self, make, model, year, capacity):
        super().__init__(make, model, year)
        self.capacity = capacity

    def calculate_mileage(self):
        self.mileage = 1.5 * self.capacity

    def calculate_towing_capacity(self):
        self.towing_capacity = 1.25 * self.capacity


class Truck(Vehicle):
    def __init__(self, make, model, year, capacity):
        super().__init__(make, model, year)
        self.capacity = capacity

    def calculate_mileage(self):
        self.mileage = 5 * self.capacity

    def calculate_towing_capacity(self):
        self.towing_capacity = 10 * self.capacity


car_instance = Car("Toyota", "Corolla", 2023, 5)
motorcycle_instance = Motorcycle("Harley-Davidson", "Rapid", 2023, 1)
truck_instance = Truck("Volvo", "Big", 2023, 8)

car_instance.calculate_mileage()
car_instance.calculate_towing_capacity()

motorcycle_instance.calculate_mileage()
motorcycle_instance.calculate_towing_capacity()

truck_instance.calculate_mileage()
truck_instance.calculate_towing_capacity()

print("Car Mileage:", car_instance.mileage)
print("Car Towing Capacity:", car_instance.towing_capacity)

print("Motorcycle Mileage:", motorcycle_instance.mileage)
print("Motorcycle Towing Capacity:", motorcycle_instance.towing_capacity)

print("Truck Mileage:", truck_instance.mileage)
print("Truck Towing Capacity:", truck_instance.towing_capacity)
