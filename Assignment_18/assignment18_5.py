
def is_prime(num):
    if num < 2:
        return False
    if num == 2:
        return True
    if num % 2 == 0:
        return False
    for i in range(3, int(num ** 0.5) + 1, 2):
        if num % i == 0:
            return False
    return True


def main():
    # Accept number of elements from user
    numberOfElements = int(input("Enter the number of elements: "))
    
    # Accept that many elements from user
    numbers = []
    print(f"Enter {numberOfElements} numbers:")
    for i in range(numberOfElements):
        num = int(input(f"Element {i+1}: "))
        numbers.append(num)
    
    # Find prime numbers and calculate their sum
    prime_sum = 0

    
    for num in numbers:
        if is_prime(num):
            prime_sum += num
    
    print(f"Sum of prime numbers: {prime_sum}")

    
   

if __name__ == "__main__":
    main()