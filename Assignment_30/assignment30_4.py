import os

def main():
    existing_file = input("Enter the existing file name: ")
    new_file = input("Enter the new file name: ")
    
    # Use walk method to find the existing file
    found = False
    filepath = None
    
    for root, dirs, files in os.walk('.'):
        if existing_file in files:
            found = True
            filepath = os.path.join(root, existing_file)
            print(f"Found '{existing_file}' at: {filepath}")
            break
    
    if not found:
        print(f"File '{existing_file}' does not exist")
        return
    
    try:
        # Read content from existing file
        with open(filepath, 'r') as file:
            contents = file.read()
        
        # Write content to new file
        with open(new_file, 'w') as file:
            file.write(contents)
        
        print(f"Successfully copied contents from '{existing_file}' to '{new_file}'")
        
    except Exception as e:
        print(f"Error: {e}")
  
if __name__ == "__main__":
    main()