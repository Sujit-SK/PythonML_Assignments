count = 0

def displayPattern(value):
    global count
    for i in range(1,value+1):
        print(i,end="")
        count += 1
        
        if i == value and count != value * value:
            print(end="\n")
            displayPattern(i)
            


def main():
    no = int(input("Enter the number: "))

    displayPattern(no) 

    
   

if __name__ == "__main__":
    main()