
def main():
    # Accept number of elements from user
    numberOfElements = int(input("Enter the number of elements: "))
    
    # Accept that many elements from user
    numbers = []
    print(f"Enter {numberOfElements} numbers:")
    for i in range(numberOfElements):
        num = int(input(f"Element {i+1}: "))
        numbers.append(num)
    
    # Accept the number to search
    search_num = int(input("Enter the number to search: "))
    
    # Count frequency of that number
    frequency = 0
    for num in numbers:
        if num == search_num:
            frequency += 1
    
    print(f"Frequency of {search_num} in the list: {frequency}")

    
   

if __name__ == "__main__":
    main()