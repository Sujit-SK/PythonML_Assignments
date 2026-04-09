def decimalToBinary(no):
    binary = ""
    
    if no == 0:
        binary = "0"
    else:
        while no > 0:
            remainder = no % 2
            binary = str(remainder) + binary
            no = no // 2
    
    print(f"Binary equivalent: {binary}")


def main():
    no = int(input("Enter the number: "))
    decimalToBinary(no)
    
if __name__ == "__main__":
    main()