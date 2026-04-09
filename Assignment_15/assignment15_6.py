
from functools import reduce
def main():
    no = input("Enter numbers: ")

    numbers = list(map(int, no.split()))
    minimum_no = reduce(lambda x, y: x if x < y else y, numbers)


    print(minimum_no)

if __name__ == "__main__":
    main()