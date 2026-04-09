import threading


def calculate_even_factors(num):
    sum_even = 0
    for i in range(1, num + 1):
        if num % i == 0 and i % 2 == 0:
            sum_even += i
    print(f"Sum of even factors: {sum_even}")


def calculate_odd_factors(num):
    sum_odd = 0
    for i in range(1, num + 1):
        if num % i == 0 and i % 2 != 0:
            sum_odd += i
    print(f"Sum of odd factors: {sum_odd}")


def main():
    no = int(input("Enter the number: "))
    
    # Create threads
    thread1 = threading.Thread(target=calculate_even_factors, args=(no,))
    thread2 = threading.Thread(target=calculate_odd_factors, args=(no,))
    
    # Start threads
    thread1.start()
    thread2.start()
    
    # Wait for threads to complete
    thread1.join()
    thread2.join()
    
    print("Message from main thread: All threads completed successfully")
    print("Exiting from main thread")


if __name__ == "__main__":
    main()