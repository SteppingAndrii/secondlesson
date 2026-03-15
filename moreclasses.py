class Human:
    def __init__(self, name="Human"):
        self.name = name

class Car:
    def __init__(self, brand):
        self.brand = brand
        self.passengers = []

    def add_passengers(self, *args):
        for passenger in args:
            self.passengers.append(passenger)

    def print_passengers_names(self):
        if self.passengers:
            print(f"Names of {self.brand} passengers:")
            for passenger in self.passengers:
                print(passenger.name)
        else:
            print(f"No passengers found in {self.brand}")

nick = Human("Nick")
kate = Human("Kate")
my_car = Car("Bugatti")
my_car.add_passengers(nick, kate)
my_car.print_passengers_names()