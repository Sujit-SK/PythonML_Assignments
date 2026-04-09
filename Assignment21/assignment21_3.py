import threading

# Shared variable
counter = 0

# Lock to avoid race conditions
lock = threading.Lock()


def increment_counter(thread_name, increments):
    global counter
    for i in range(increments):
        # Acquire lock before modifying shared variable
        lock.acquire()
        counter += 1
        lock.release()
    print(f"{thread_name} completed {increments} increments")


def main():
    global counter
    
    # Number of increments per thread
    increments_per_thread = 1000
    
    # Create multiple threads
    thread1 = threading.Thread(target=increment_counter, args=("Thread-1", increments_per_thread))
    thread2 = threading.Thread(target=increment_counter, args=("Thread-2", increments_per_thread))
    thread3 = threading.Thread(target=increment_counter, args=("Thread-3", increments_per_thread))
    thread4 = threading.Thread(target=increment_counter, args=("Thread-4", increments_per_thread))
    
    # Start all threads
    thread1.start()
    thread2.start()
    thread3.start()
    thread4.start()
    
    # Wait for all threads to complete
    thread1.join()
    thread2.join()
    thread3.join()
    thread4.join()
    
    # Display final counter value
    print(f"\nFinal counter value: {counter}")
    print(f"Expected value: {4 * increments_per_thread}")


if __name__ == "__main__":
    main()
