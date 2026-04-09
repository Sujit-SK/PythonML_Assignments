square = lambda x: x * x

def main():
    no = input("Enter numbers: ")

    numbers = list(map(int, no.split()))
    squared_numbers = list(map(square, numbers))

    print(squared_numbers)

if __name__ == "__main__":
    main()
