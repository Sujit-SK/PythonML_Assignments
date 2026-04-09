def checkSum(no):
    if no % 2 == 0:
        print("Even number")
    else:
        print("Odd number")

def main():
    no = int(input("Enter the number: "))
    checkSum(no)


if __name__ == "__main__":
    main()