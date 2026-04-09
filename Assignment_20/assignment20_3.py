import threading


def calculate_even_sum(numbers):
    sum_even = 0
    for num in numbers:
        if num % 2 == 0:
            sum_even += num
    print(f"Sum of even numbers: {sum_even}")


def calculate_odd_sum(numbers):
    sum_odd = 0
    for num in numbers:
        if num % 2 != 0:
            sum_odd += num
    print(f"Sum of odd numbers: {sum_odd}")


def main():
    # Accept list from user
    user_input = input("Enter numbers separated by space: ")
    numbers = list(map(int, user_input.split()))
    
    # Create threads
    thread1 = threading.Thread(target=calculate_even_sum, args=(numbers,))
    thread2 = threading.Thread(target=calculate_odd_sum, args=(numbers,))
    
    # Start threads
    thread1.start()
    thread2.start()
    
    # Wait for threads to complete
    thread1.join()
    thread2.join()
    
    print("Both calculations completed")


if __name__ == "__main__":
    main()