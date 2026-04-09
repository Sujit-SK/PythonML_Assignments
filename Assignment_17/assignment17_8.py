count= 1

def displayPattern(value):
    global count
    maxloop = value - count
    value1 = value -maxloop
    
    
    for i in range(1, value1+1):
        print(i,end="")
    
    count += 1

    if count != value + 1:
        print(end="\n")
        displayPattern(value)

       
        
  
            


def main():
    no = int(input("Enter the number: "))

    displayPattern(no) 

    
   

if __name__ == "__main__":
    main()