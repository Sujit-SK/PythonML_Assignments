divisibleBy = lambda a: True if a % 5 == 0 else False

def main():
    no = int(input("Enter the number: "))
    
    print("Result is:", divisibleBy(no))
   
    
if __name__ == "__main__":
    main()