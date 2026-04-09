class Demo:
    # Class variable
    
    def __init__(self, num1=0, num2=0):
        # Instance variables
        self.num1 = num1
        self.num2 = num2
        self.result = 0
        

    def accept(self):
        self.num1 = int(input("Enter first number: "))
        self.num2 = int(input("Enter second number: "))
    
    def addition(self):
        self.result = self.num1 + self.num2
        print(f"Addition: {self.num1} + {self.num2} = {self.result}")
    
    def subtraction(self):
        self.result = self.num1 - self.num2
        print(f"Subtraction: {self.num1} - {self.num2} = {self.result}")
    
    def multiplication(self):
        self.result = self.num1 * self.num2
        print(f"Multiplication: {self.num1} * {self.num2} = {self.result}")
    
    def division(self):
        if self.num2 != 0:
            self.result = self.num1 / self.num2
            print(f"Division: {self.num1} / {self.num2} = {self.result}")
        else:
            print("Error: Division by zero is not allowed")
        
    def display(self):
        print("Calculator Results:")
        print("Number 1:", self.num1)
        print("Number 2:", self.num2)
        print("Last Result:", self.result)

def main():
    # Create first object
    obj1 = Demo()
    obj1.accept()
    obj1.addition()
    obj1.subtraction()
    obj1.multiplication()
    obj1.division()
    
    print()
    
    # Create second object
    obj2 = Demo()
    obj2.accept()
    obj2.addition()
    obj2.subtraction()
    obj2.multiplication()
    obj2.division()
    
    

if __name__ == "__main__":
    main()