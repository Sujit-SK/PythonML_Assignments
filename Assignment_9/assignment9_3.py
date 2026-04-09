def main():
    no = int(input("Enter the number: "))
    
    sum_digits = 0
    
    for i in range(len(str(no))):
        digit = int(str(no)[i])
        sum_digits = sum_digits + digit
    
    print(f"Sum of digits: {sum_digits}")



if __name__ == "__main__":
    main()