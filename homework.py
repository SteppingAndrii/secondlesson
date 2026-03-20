class Student:
    def __init__(self, name):
        self.name = name
        self.grade = 88
    def study(self):
        print(f"{self.name}'s grades are {self.grade}%")

class Worker:
    def __init__(self, name):
        self.name = name
        self.job = "Programmer"
        self.salary = 4500
    def work(self):
        print(f"{self.name} works as a {self.job} and earns {self.salary}$ per month")

class Athlete:
    def __init__(self, name):
        self.name = name
        self.sport = "Football"
        self.energy = 89
    def train(self):
        print(f"{self.name}'s sport is {self.sport} and {self.name}'s energy is {self.energy}%")

class Person(Student, Worker, Athlete):
    def __init__(self, name):
        Student.__init__(self, name)
        Worker.__init__(self, name)
        Athlete.__init__(self, name)
    def show_all_info(self):
        print(f"Your info:\nName: {self.name}\nGrade: {self.grade}\nJob: {self.job}\nSport: {self.sport}\nEnergy: {self.energy}%")

p = Person("Larry")
p.show_all_info()
