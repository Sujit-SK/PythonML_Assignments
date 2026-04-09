
def main():
    # Accept list from user
    user_input = input("Enter numbers separated by space: ")
    numbers = list(map(int, user_input.split()))
    
    # Calculate sum
    total = 0
    for num in numbers:
        total += num
    
    print("Sum of the list:", total)

    
   

if __name__ == "__main__":
    main()
