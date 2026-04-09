def main():
    num = int(input("Enter the number: "))
    
    counter = 0
    
    for digit in str(num):
        counter += 1
    
    print(f"Number of digits: {counter}")


if __name__ == "__main__":
    main()