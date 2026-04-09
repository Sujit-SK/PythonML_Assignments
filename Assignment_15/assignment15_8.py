
def main():
    no = input("Enter Values: ")

    numbers = list(map(int, no.split()))
    divisible = list(filter(lambda x: x % 3 == 0 and x % 5 ==0, numbers))

    print(divisible)



if __name__ == "__main__":
    main()