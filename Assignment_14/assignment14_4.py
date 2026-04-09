
minimumNo = lambda a, b: a if a < b else b

def main():
    no1 = int(input("Enter first number: "))
    no2 = int(input("Enter second number: "))
 
    print("minimum number is:",minimumNo(no1,no2))
   
    
if __name__ == "__main__":
    main()