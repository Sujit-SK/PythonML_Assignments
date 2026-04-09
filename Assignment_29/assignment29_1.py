import os

def main():
    filename = input("Enter the file name: ")
    
    found = False
    for root, dirs, files in os.walk('.'):
        if filename in files:
            found = True
            print(f"File '{filename}' is present in the directory: {root}")
            break
    
    if not found:
        print(f"File '{filename}' is not present in the current directory")
  
if __name__ == "__main__":
    main()
