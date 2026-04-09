def main():
    no = int(input("Enter the number: "))
    
    sum_natural = 0
    
    for i in range(1, no + 1):
        sum_natural = sum_natural + i
    
    print(sum_natural)



if __name__ == "__main__":
    main()