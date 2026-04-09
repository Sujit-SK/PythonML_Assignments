
def main():
    words = input("Enter Values: ")

    words = words.split()
    greater_than_5 = list(filter(lambda x: len(x) > 5, words))

    print(greater_than_5)



if __name__ == "__main__":
    main()