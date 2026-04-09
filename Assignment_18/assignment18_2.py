
def maximum(data):
    # Calculate sum
    max_no = data[0]
    for num in data:
        if num > max_no:
            max_no = num
    return max_no


def main():
    # Accept list from user
    user_input = input("Enter numbers separated by space: ")
    numbers = list(map(int, user_input.split()))
    
    maximumNo = maximum(numbers)
    
    print("Maximum number is:", maximumNo)

    
   

if __name__ == "__main__":
    main()