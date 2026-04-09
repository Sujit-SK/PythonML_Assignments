import os

def main():
    filename = input("Enter the file name: ")
   
    
    # Check if file exists
    if not os.path.isfile(filename):
        print(f"File '{filename}' does not exist")
        return
    
    try:
        # Display file line by line
        with open(filename, 'r') as file:
            line_number = 1
            for line in file:
                print(f"Line {line_number}: {line}", end='')
                line_number += 1
        
    except Exception as e:
        print(f"Error: {e}")
  
if __name__ == "__main__":
    main()