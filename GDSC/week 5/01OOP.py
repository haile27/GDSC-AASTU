'''
class person:
    def __init__(self, name, age) -> None:
        self.name = name
        self.age = age

    def say_name(self)    :
        return f"My name is {self.name}"
p1 = person('haillu')
print("Name:",p1.say_name)

'''
class rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length*self.width
    def perimeter(self):
        return 2(self.lengtn + self.width)
    
r1 =rectangle(3, 5)
print("Area",r1.area) 

print("Perimete:",r1.perimeter)   
 
#3
class shape:
    
    def __init__(self, color):
        self.color =color

    def get_color(self):
        return self.color
    
    def area(self):
        pass
class rectangle(shape):
    def __init__(self, color, length, width):
        super().__init__(color)
        self.length = length
        self.width = width
    def area(self):
        return self.length*self.width

    class circle(shape):
        def __init__(self, color, radius):
            super().__init__(color)
            self.radius= radius
        def area(self):
            return 3.14*(self.radius**2)    




    
    
   