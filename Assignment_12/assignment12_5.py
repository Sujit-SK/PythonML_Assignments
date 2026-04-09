
def divisible(value1):
    if(value1 % 3 == 0 and value1 % 5 == 0):
        print(f"{value1} is divisible by 3 and 5")
    else:
        print(f"{value1} is not divisible by 3 and 5")
    

def main():
    no =int(input("Enter the number: "))
    divisible(no)
   
    
if __name__ == "__main__":
    main()