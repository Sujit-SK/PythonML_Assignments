import threading


def displayNumber():
    for i in range(1, 51):
        print(i)
 

def displayReverseNumber():
    for i in range(50, 0, -1):
        print(i)



def main():
    thread1 = threading.Thread(target=displayNumber)
    thread2 = threading.Thread(target=displayReverseNumber)
    
    # Start thread1 and wait for it to complete
    thread1.start()
    thread1.join()
    
    # Start thread2 after thread1 completes
    thread2.start()
    thread2.join()
    
    print("All threads completed")


if __name__ == "__main__":
    main()