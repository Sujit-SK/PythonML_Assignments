def main():
    no = int(input("Enter the number: "))
    
    factorial  = 1
    
    for i in range(1, no + 1):
        factorial = factorial * i
    
    print("factorial is :",factorial)



if __name__ == "__main__":
    main()