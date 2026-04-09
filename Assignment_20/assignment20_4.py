import threading


def count_small_letters(text):
    count = 0
    for char in text:
        if char.islower():
            count += 1
    thread = threading.current_thread()
    print(f"Small letters count: {count}")
    print(f"Thread Name: {thread.name}, Thread ID: {thread.ident}")


def count_capital_letters(text):
    count = 0
    for char in text:
        if char.isupper():
            count += 1
    thread = threading.current_thread()
    print(f"Capital letters count: {count}")
    print(f"Thread Name: {thread.name}, Thread ID: {thread.ident}")


def count_digits(text):
    count = 0
    for char in text:
        if char.isdigit():
            count += 1
    thread = threading.current_thread()
    print(f"Digits count: {count}")
    print(f"Thread Name: {thread.name}, Thread ID: {thread.ident}")


def main():
    # Accept string from user
    text = input("Enter a string: ")
    
    # Create threads
    thread1 = threading.Thread(target=count_small_letters, args=(text,))
    thread2 = threading.Thread(target=count_capital_letters, args=(text,))
    thread3 = threading.Thread(target=count_digits, args=(text,))
    
    # Start threads
    thread1.start()
    thread2.start()
    thread3.start()
    
    # Wait for threads to complete
    thread1.join()
    thread2.join()
    thread3.join()
    
    print("All threads completed")


if __name__ == "__main__":
    main()