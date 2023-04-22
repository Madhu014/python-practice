#Create a Cricle class and intialize it with radius. Make two methods getArea and getCircumference inside this class.
class Circle:
    def __init__(self,radius):
        self.radius=radius
    def get_area(self):
        return 3.14*self.radius**2
    def get_circumference(self):
        return 2*3.14*self.radius
obj_1=Circle(6)
print(obj_1.get_area())
print(obj_1.get_circumference())