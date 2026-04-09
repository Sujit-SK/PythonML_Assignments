def primeNumber(value):
    if value < 2: return False
    for i in range(2, int(value ** 0.5) + 1):
        if value % i == 0:
            return False
    return True


def main():
    no = int(input("Enter the number: "))

    result = primeNumber(no) 

    print(result)
    
   

if __name__ == "__main__":
    main()