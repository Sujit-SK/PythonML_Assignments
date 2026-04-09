
def addition(no1, no2):
    return no1 + no2

def subtraction(no1, no2):
    return no1 - no2

def multiplication(no1, no2):
    return no1 * no2

def division(no1, no2):
    if no2 != 0: return no1 / no2

def main():
    no1 = int(input("Enter the first number: "))
    no2 = int(input("Enter the second number: "))

    add = addition(no1, no2)
    print(add)

    sub = subtraction(no1, no2)
    print(sub)

    mult = multiplication(no1, no2)
    print(mult)

    div = division(no1, no2)
    print(div)    
    
   

if __name__ == "__main__":
    main()
