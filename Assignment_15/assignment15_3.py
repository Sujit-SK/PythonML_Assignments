def main():
    no = input("Enter numbers: ")

    numbers = list(map(int, no.split()))
    odd_numbers = list(filter(lambda x: x % 2 != 0, numbers))

    print(odd_numbers)

if __name__ == "__main__":
    main()