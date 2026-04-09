def addition(a, b):
    return a + b

def main():
    no1 = int(input("Enter the first number: "))
    no2 = int(input("Enter the second number: "))
    result = addition(no1, no2)

    print("The addidition is : ", result)

if __name__ == "__main__":
    main()