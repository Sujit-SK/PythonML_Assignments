
def checkGreater(value1, value2):
    if(value1 > value2):
        print(f"{value1} is greater than {value2}")
    elif(value2 > value1):
        print(f"{value2} is greater than {value1}")
    else:
        print("Both numbers are equal")

def main():
    no1 =int(input("Enter first number: "))
    no2 =int(input("Enter second number: "))

    checkGreater(no1, no2)
    
if __name__ == "__main__":
    main()