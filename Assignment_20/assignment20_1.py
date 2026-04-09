import threading


def display_even():
    for i in range(1, 11):
        if(i % 2 == 0):
            print(i)


def display_odd():
    for i in range(10):
        if(i % 2 != 0):
            print(i)


def main():
    # Create threads
    thread1 = threading.Thread(target=display_even)
    thread2 = threading.Thread(target=display_odd)
    
    # Start threads
    thread1.start()
    thread2.start()
    
    # Wait for threads to complete
    thread1.join()
    thread2.join()
    
    print("Both threads completed")


if __name__ == "__main__":
    main()
