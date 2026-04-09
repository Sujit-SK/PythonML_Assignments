def display(value):
    for i in range(value):
        print("*" * value)


def main():
    value = int(input("Enter the number: "))

    display(value) 
    
   

if __name__ == "__main__":
    main()