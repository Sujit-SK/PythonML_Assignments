
def displayPattern(value):
    for i in range(value):
        for j in range(1,value+1):
            print(j,end="")
        print()
        
            


def main():
    no = int(input("Enter the number: "))

    displayPattern(no) 

    
   

if __name__ == "__main__":
    main()