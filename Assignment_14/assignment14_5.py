
checkEven = lambda a: True if a % 2 == 0 else False

def main():
    no = int(input("Enter the number: "))
    
    print("The number is:", checkEven(no))
   
    
if __name__ == "__main__":
    main()