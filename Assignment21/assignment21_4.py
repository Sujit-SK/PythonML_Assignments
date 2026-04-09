import threading

# Dictionary to store results from threads
results = {}


def calculate_sum(numbers):
    total = 0
    for num in numbers:
        total += num
    results['sum'] = total
  


def calculate_product(numbers):
    product = 1
    for num in numbers:
        product *= num
    results['product'] = product



def main():
    # Accept list from user
    user_input = input("Enter numbers separated by space: ")
    numbers = list(map(int, user_input.split()))
    
    # Create threads
    thread1 = threading.Thread(target=calculate_sum, args=(numbers,))
    thread2 = threading.Thread(target=calculate_product, args=(numbers,))
    
    # Start threads
    thread1.start()
    thread2.start()
    
    # Wait for threads to complete
    thread1.join()
    thread2.join()
    
    # Display results in main thread
    print("\n--- Results from Main Thread ---")
    print(f"Sum of elements: {results['sum']}")
    print(f"Product of elements: {results['product']}")


if __name__ == "__main__":
    main()

