from functools import reduce

def main():
    no = input("Enter Values: ")

    numbers = list(map(int, no.split()))
    product = reduce(lambda x,y: x * y, numbers)

    print(product)



if __name__ == "__main__":
    main()