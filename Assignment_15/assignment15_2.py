def main():
    no = input("Enter numbers: ")

    numbers = list(map(int, no.split()))
    even_numbers = list(filter(lambda x: x % 2 == 0, numbers))

    print(even_numbers)

if __name__ == "__main__":
    main()