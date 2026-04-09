
from functools import reduce
def main():
    no = input("Enter numbers: ")

    numbers = list(map(int, no.split()))
    addition = reduce(lambda x,y: x + y , numbers)

    print(addition)

if __name__ == "__main__":
    main()