import random

class Human:
    def __init__(self, name="Human", age=None, job=None, home=None, car=None):
        self.name = name
        self.age = age
        self.job = job
        self.home = home
        self.car = car
        self.money = 100
        self.happiness = 50
        self.saturation = 50

    def get_home(self):
        self.home = House()

    def get_car(self, brand_of_car):
        self.car = TheCar(brand_of_car)

    def get_job(self, job_list):
        self.job = TheJob(job_list)

    def go_to_job(self):
        if self.job:
            print(f"{self.name} is going to work as a {self.job.title}.")
            self.money += self.job.salary
            self.happiness += self.job.happiness_change
            self.saturation -= self.job.saturation_change

            self.happiness = max(0, min(100, self.happiness))
            self.saturation = max(0, min(100, self.saturation))

            print(f"Money: {self.money}, Happiness: {self.happiness}, Saturation: {self.saturation}")
        else:
            print(f"{self.name} has no job to go to!")

    def eat_food(self, amount=10):
        self.saturation = min(100, self.saturation + amount)
        print(f"{self.name} ate food. Saturation is now {self.saturation}.")

    def relax(self, amount=10):
        self.happiness = min(100, self.happiness + amount)
        print(f"{self.name} is relaxing. Happiness is now {self.happiness}.")

class TheJob:
    def __init__(self, job_list):
        self.title = random.choice(list(job_list.keys()))
        self.salary = job_list[self.title]["salary"]
        self.happiness_change = job_list[self.title]["happiness_change"]
        self.saturation_change = job_list[self.title]["saturation_change"]

class TheCar:
    def __init__(self, brand_list):
        self.brand = random.choice(list(brand_list))
        self.fuel = brand_list[self.brand]["fuel"]
        self.horsepower = brand_list[self.brand]["horsepower"]
        self.turn_signal_usage = brand_list[self.brand]["turn_signal_usage"]

class House:
    def __init__(self):
        self.mess = 0
        self.food = 50

    def clean_house(self):
        self.mess = max(0, self.mess - 10)
        print(f"The house has been cleaned. Cleanliness is now {self.mess}.")

    def stock_food(self, amount=10):
        self.food = min(100, self.food + amount)
        print(f"Food stocked. Current food level is {self.food}.")

job_list = {
    "Software Developer": {
        "salary": 2000,
        "happiness_change": 10,
        "saturation_change": 5
    },
    "Teacher": {
        "salary": 1200,
        "happiness_change": 20,
        "saturation_change": 10
    },
    "Chef": {
        "salary": 1500,
        "happiness_change": 30,
        "saturation_change": 15
    },
    "Construction Worker": {
        "salary": 1800,
        "happiness_change": 5,
        "saturation_change": 20
    }
}

# Car brands
brand_of_car = {
    "Bugatti": {
        "fuel": 70,
        "horsepower": 1500,
        "turn_signal_usage": 1654000
    },
    "BMW": {
        "fuel": 100,
        "horsepower": 720,
        "turn_signal_usage": 0
    },
    "Porsche": {
        "fuel": 50,
        "horsepower": 520,
        "turn_signal_usage": 150714000
    }
}

john = Human(name="John Doe", age=30)

john.get_home()

john.get_job(job_list)

print(f"Stats for {john.name}:")
print(f"Money: {john.money}, Happiness: {john.happiness}, Saturation: {john.saturation}")

john.go_to_job()

john.eat_food(15)
john.relax(20)

john.home.clean_house()
john.home.stock_food(20)

john.get_car(brand_of_car)

print(f"\n{john.name}'s car details:")
print(f"Car Brand: {john.car.brand}, Fuel: {john.car.fuel}, Horsepower: {john.car.horsepower}")

print(f"\nFinal stats for {john.name}:")
print(f"Money: {john.money}, Happiness: {john.happiness}, Saturation: {john.saturation}")