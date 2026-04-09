import threading


def maximumNumber(numbers):
    max_num = numbers[0]
    for num in numbers:
        if num > max_num:
            max_num = num
    print(f"Maximum number: {max_num}")


def minimumNumber(numbers):
    min_num = numbers[0]
    for num in numbers:
        if num < min_num:
            min_num = num
    print(f"Minimum number: {min_num}")


def main():
    # Accept list from user
    user_input = input("Enter numbers separated by space: ")
    numbers = list(map(int, user_input.split()))
    
    # Create threads
    thread1 = threading.Thread(target=maximumNumber, args=(numbers,))
    thread2 = threading.Thread(target=minimumNumber, args=(numbers,))
    
    thread1.start()
    thread2.start()

    thread1.join()
    thread2.join()
    
    print("All threads completed")


if __name__ == "__main__":
    main()
