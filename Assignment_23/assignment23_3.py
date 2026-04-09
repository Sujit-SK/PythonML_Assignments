class Number:
    
    def __init__(self, num):
        # Instance variable
        self.num = num
       
    def checkprime(self):
        if self.num < 2:
            print(f"{self.num} is not a prime number")
            return False
        if self.num == 2:
            print(f"{self.num} is a prime number")
            return True
        if self.num % 2 == 0:
            print(f"{self.num} is not a prime number")
            return False
        for i in range(3, int(self.num ** 0.5) + 1, 2):
            if self.num % i == 0:
                print(f"{self.num} is not a prime number")
                return False
        print(f"{self.num} is a prime number")
        return True
    
    def checkperfect(self):
        sum_factors = 0
        for i in range(1, self.num):
            if self.num % i == 0:
                sum_factors += i
        if sum_factors == self.num:
            print(f"{self.num} is a perfect number")
            return True
        else:
            print(f"{self.num} is not a perfect number")
            return False
    
    def factors(self):
        print(f"Factors of {self.num}:")
        for i in range(1, self.num + 1):
            if self.num % i == 0:
                print(i, end=" ")
        print()
    
    def sumFactors(self):
        sum_factors = 0
        for i in range(1, self.num + 1):
            if self.num % i == 0:
                sum_factors += i
        print(f"Sum of factors of {self.num}: {sum_factors}")
        return sum_factors

def main():
    # Create first object
    num1 = int(input("Enter first number: "))
    obj1 = Number(num1)
    obj1.checkprime()
    obj1.checkperfect()
    obj1.factors()
    obj1.sumFactors()
    
    print()
    
    # Create second object
    num2 = int(input("Enter second number: "))
    obj2 = Number(num2)
    obj2.checkprime()
    obj2.checkperfect()
    obj2.factors()
    obj2.sumFactors()
    
    print()
    
    # Create third object
    num3 = int(input("Enter third number: "))
    obj3 = Number(num3)
    obj3.checkprime()
    obj3.checkperfect()
    obj3.factors()
    obj3.sumFactors()

if __name__ == "__main__":
    main()