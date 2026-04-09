def addition(value1,value2):
    return value1 + value2

def subtraction(value1,value2):
    return value1 - value2

def multiplication(value1,value2):
    return value1 * value2

def division(value1,value2):
    return value1 / value2


def main():
    no1 = int(input("Enter first number: "))
    no2 = int(input("Enter second number: "))
    add = addition(no1,no2)
    sub = subtraction(no1,no2)
    mult = multiplication(no1,no2)
    div = division(no1,no2)

    print(f"Addition: {add}")
    print(f"Subtraction: {sub}")
    print(f"Multiplication: {mult}")
    print(f"Division: {div}")
   
    
if __name__ == "__main__":
    main()