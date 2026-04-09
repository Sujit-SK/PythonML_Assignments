from functools import reduce


def main():
    user_input = input("Enter numbers separated by space: ")
    numbers = list(map(int, user_input.split()))

    filtered_numbers = list(filter(lambda x: x % 2 == 0, numbers))
    
    print("Even numbers:", filtered_numbers)

    square = list(map(lambda x: x * x, filtered_numbers))
    print("Square:", square)

    result = reduce(lambda x, y: x + y, square)
    print("Addition numbers:", result)
   

if __name__ == "__main__":
    main()