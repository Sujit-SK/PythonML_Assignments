
def main():
    no = input("Enter Values: ")

    numbers = list(map(int, no.split()))
    count_even_numbers = len(list(filter(lambda x:  x % 2 == 0, numbers)))

    print(count_even_numbers)



if __name__ == "__main__":
    main()