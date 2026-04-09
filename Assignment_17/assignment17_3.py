def factorial(value):
    return value * factorial(value - 1) if value > 1 else 1


def main():
    no = int(input("Enter the number: "))

    result = factorial(no) 

    print(result)
    
   

if __name__ == "__main__":
    main()