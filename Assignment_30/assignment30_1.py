import os

def main():
    filename = input("Enter the file name: ")
   
    
    # Check if file exists
    if not os.path.isfile(filename):
        print(f"File '{filename}' does not exist")
        return
    
    try:
        # Read content from file
        counter = 0

        with open(filename, 'r') as file:
            for line in file:
                counter +=1
        
        print("Total Number of lines in the file:", counter)
        
    except Exception as e:
        print(f"Error: {e}")
  
if __name__ == "__main__":
    main()
