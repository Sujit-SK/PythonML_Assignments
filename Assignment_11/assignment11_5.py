def checkGrade(no):
    
    
    if(no >= 75):
        print("Distinction")
    elif(no >= 60):
        print("First Class")
    elif(no >= 50):
        print("Second Class")
    elif(no < 50):
        print("Fail")

    



def main():
    no = int(input("Enter the number: "))
    checkGrade(no)
    
if __name__ == "__main__":
    main()