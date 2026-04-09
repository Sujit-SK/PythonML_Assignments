
def main():
    no = int(input("Enter the number: "))

    sum_digits = 0
    temp = abs(no)
    
    while temp > 0:
        digit = temp % 10
        sum_digits += digit
        temp = temp // 10
    
    print(sum_digits)

    
   

if __name__ == "__main__":
    main()