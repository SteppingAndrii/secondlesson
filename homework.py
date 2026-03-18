name = "Larry"

class Student:
    def __init__(self):
        self.grade = 88

    def study(self):
        print(f"{name}'s grades are {self.grade}%")


class Worker:
    def __init__(self):
        self.job = "Programmer"
        self.salary = 4500

    def work(self):
        print(f"{name} works as a {self.job} and earns {self.salary}$ per month")


class Athlete:
    def __init__(self):
        self.sport = "Football"
        self.energy = 89
  
    def train(self):
        print(f"{name}'s sport is {self.sport} and {name}'s energy is {self.energy}%")


# All in one person
class Person(Student, Worker, Athlete):
    def __init__(self):
        Student.__init__(self)
        Worker.__init__(self)
        Athlete.__init__(self)

    def show_all_info(self):
        print(f"Your info:\nName: {name}\nGrade: {self.grade}\nJob: {self.job}\nSport: {self.sport}\nEnergy: {self.energy}%")

p = Person()

# p.study()     # from Student
# p.work()      # from Worker
# p.train()     # from Athlete

# All in one info
p.show_all_info()
