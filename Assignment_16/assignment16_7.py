
def divisible(no):
    return no % 5 == 0

def main():
    no = int(input("Enter the number: "))
    
    result = divisible(no)
    print(result)
   

if __name__ == "__main__":
    main()