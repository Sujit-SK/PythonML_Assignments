class Demo:
    # Class variable
    PI = 3.14
    
    def __init__(self, radius=0):
        # Instance variables
        self.radius = radius
        self.area = 0
        self.circumference = 0
        Demo.counter += 1

    def accept(self):
        self.radius = int(input("Enter the radius of the circle: "))
    
    def calculate_area(self):
        self.area = Demo.PI * (self.radius ** 2)
    
    def calculate_circumference(self):
        self.circumference = 2 * Demo.PI * self.radius
        
    def display(self):
        print("Circle Details:")
        print("Radius:", self.radius)
        print("Area:", self.area)
        print("Circumference:", self.circumference)

def main():
    # Create first circle object
    obj1 = Demo()
    obj1.accept()
    obj1.calculate_area()
    obj1.calculate_circumference()
    obj1.display()
    
    print()
    
    # Create second circle object
    obj2 = Demo()
    obj2.accept()
    obj2.calculate_area()
    obj2.calculate_circumference()
    obj2.display()
    
    print()
    
    # Create third circle object
    obj3 = Demo()
    obj3.accept()
    obj3.calculate_area()
    obj3.calculate_circumference()
    obj3.display()
    
    

if __name__ == "__main__":
    main()