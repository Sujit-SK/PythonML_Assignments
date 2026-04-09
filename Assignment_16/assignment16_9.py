
def even_number(no):
    for i in range(1, no+1):
         if i % 2 == 0:
          print(i)
  

def main():
    no = int(input("Enter the number: "))
    
    even_number(no)  
   

if __name__ == "__main__":
    main()