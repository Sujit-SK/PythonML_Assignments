import threading


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


def primeNumber(numbers):
    print("Prime numbers:")
    for num in numbers:
        if is_prime(num):
            print(num)


def nonPrimeNumbers(numbers):
    print("Non-prime numbers:")
    for num in numbers:
        if not is_prime(num):
            print(num)


def main():
    # Accept list from user
    user_input = input("Enter numbers separated by space: ")
    numbers = list(map(int, user_input.split()))
    
    # Create threads
    thread1 = threading.Thread(target=primeNumber, args=(numbers,))
    thread2 = threading.Thread(target=nonPrimeNumbers, args=(numbers,))
    
    thread1.start()
    thread2.start()

    thread1.join()
    thread2.join()
    
    print("All threads completed")


if __name__ == "__main__":
    main()
