def main():
    no1 = int(input("Enter the first number: "))
    no2 = int(input("Enter the second number: "))

    multiplication = lambda x,y: x * y

    print("Power of 2 is:", multiplication(no1,no2))
     
   

if __name__ == "__main__":
    main()