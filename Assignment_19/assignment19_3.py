from functools import reduce


def main():
    user_input = input("Enter numbers separated by space: ")
    numbers = list(map(int, user_input.split()))

    filtered_numbers = list(filter(lambda x: x >= 70 and x <= 90, numbers))
    
    print("Filtered numbers:", filtered_numbers)

    increase = list(map(lambda x: x + 10, filtered_numbers))
    print("Increased numbers:", increase)

    result = reduce(lambda x, y: x * y, increase)
    print("Product of numbers:", result)
   

if __name__ == "__main__":
    main()