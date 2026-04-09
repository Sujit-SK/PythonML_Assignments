greatestNumber = lambda a, b ,c: a if a > b and a > c else b if b > a and b > c else c

def main():
    no1 = int(input("Enter first number: "))
    no2 = int(input("Enter second number: "))
    no3 = int(input("Enter third number: "))
    
    print("GreatestNumber is:", greatestNumber(no1,no2,no3))
   
    
if __name__ == "__main__":
    main()