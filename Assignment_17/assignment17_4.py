def sum_of_factors(value):
    total = 0
    for i in range(1, value + 1):
        if value % i == 0:
            total += i
    return total


def main():
    no = int(input("Enter the number: "))

    result = sum_of_factors(no) 

    print(result)
    
   

if __name__ == "__main__":
    main()