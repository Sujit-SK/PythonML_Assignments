
def displayPattern(value):
   for i in range(value, 0, -1):
       print("*" * i)


def main():
    no = int(input("Enter the number: "))

    displayPattern(no) 

    
   

if __name__ == "__main__":
    main()