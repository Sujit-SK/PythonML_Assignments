
def main():
    no = int(input("Enter the number: "))

    count = 0
    temp = abs(no)
    
    # Handle special case for 0
    if temp == 0:
        count = 1
    else:
        while temp > 0:
            count += 1
            temp = temp // 10
    
    print(count)

    
   

if __name__ == "__main__":
    main()