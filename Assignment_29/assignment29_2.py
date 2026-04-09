import os

def main():
    filename = input("Enter the file name: ")
    
    found = False
    filepath = None
    
    for root, dirs, files in os.walk('.'):
        if filename in files:
            found = True
            filepath = os.path.join(root, filename)
            print(f"File '{filename}' is present in the directory: {root}")
            break
    
    if found:
        print("\n--- File Contents ---")
        try:
            with open(filepath, 'r') as file:
                contents = file.read()
                print(contents)
        except Exception as e:
            print(f"Error reading file: {e}")
    else:
        print(f"File '{filename}' is not present in the current directory")
  
if __name__ == "__main__":
    main()