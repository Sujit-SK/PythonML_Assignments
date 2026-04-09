def checkPerfect(no):
    sum_divisors = 0
    
    for i in range(1, no):
        if no % i == 0:
            sum_divisors = sum_divisors + i
    
    if sum_divisors == no:
        print(f"{no} is a perfect number")
    else:
        print(f"{no} is not a perfect number")


def main():
    no = int(input("Enter the number: "))
    checkPerfect(no)
    
if __name__ == "__main__":
    main()