
def minimum(data):
    # Calculate sum
    min_no = data[0]
    for num in data:
        if num < min_no:
            min_no = num
    return min_no


def main():
    # Accept list from user
    user_input = input("Enter numbers separated by space: ")
    numbers = list(map(int, user_input.split()))
    
    minimumNo = minimum(numbers)
    
    print("Minimum number is:", minimumNo)

    
   

if __name__ == "__main__":
    main()