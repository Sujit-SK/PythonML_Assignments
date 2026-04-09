from functools import reduce


def is_prime(num):
    if num < 2:
        return False
    if num == 2:
        return True
    if num % 2 == 0:
        return False
    for i in range(3, int(num ** 0.5) + 1, 2):
        if num % i == 0:
            return False
    return True


def main():
    user_input = input("Enter numbers separated by space: ")
    numbers = list(map(int, user_input.split()))

    filtered_numbers = list(filter(lambda x: is_prime(x), numbers))
    
    print("Prime numbers:", filtered_numbers)

    multipleBy2 = list(map(lambda x: x * 2, filtered_numbers))
    print("multipleBy2:", multipleBy2)

    result = reduce(lambda x, y: x if x > y else y, multipleBy2)
    print("Maximum number:", result)
   

if __name__ == "__main__":
    main()