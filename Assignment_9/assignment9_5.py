def main():
    no = int(input("Enter the number: "))
    
    reverse = 0
    temp = no
    
    while temp > 0:
        digit = temp % 10
        reverse = reverse * 10 + digit
        temp = temp // 10
    
    if no == reverse:
        print(f"{no} is a palindrome")
    else:
        print(f"{no} is not a palindrome")



if __name__ == "__main__":
    main()