def factors(value):
    print("Factors are: ")
    for i in range(1, value + 1):
        if value % i == 0:
            print(i)


def main():
    no = int(input("Enter first number: "))
    factors(no)
   
    
if __name__ == "__main__":
    main()