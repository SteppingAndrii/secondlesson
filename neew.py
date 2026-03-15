# class Parent:
#     pass
# class Child(Parent):
#     pass

# class Human:
#     height = 100
#     name1 = "ill"
#     name2 = "kim"
# class Student(Human):
#     pass
# class Worker(Human):
#     pass

# john = Student()
# sick = Worker()
# print(john.name1)
# print(sick.name2)


# class Human:
#     height = 100
#     saturation = 50
# class Student(Human):
#     saturation = 0
# class Worker(Human):
#     saturation = 100

# john = Student()
# sick = Worker()
# print(john.saturation)
# print(sick.saturation)


# class Grandparent:
#     height = 175
#     saturation = 100
#     age = 60
# class Parent(Grandparent):
#     age = 40
# class Child(Parent):
#     height = 120
#     def __init__(self):
#         print(self.height)
#         print(self.saturation)
#         print(self.age)

# nick = Child()



# class Class1:
#     var = 10
#     def __init__(self):
#         self.var = 20

# class Class2(Class1):
#     def __init__(self):
#         print(self.var)
#         super().__init__()
#         print(self.var)
#         print(super().var)

# hello_world = Class2()



import math

class Shape:
    def __init__(self, color="Transparent"):
        self.color = color

    def area(self):
        pass


class Circle(Shape):
    def __init__(self, radius, color="Transparent"):
        super().__init__(color)
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2


class Rectangle(Shape):
    def __init__(self, width, height, color="Transparent"):
        super().__init__(color)
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height


circle = Circle(3, "blue")
rect = Rectangle(5, 8, "purple")

print(circle.area())
print(rect.area())
print(circle.color)