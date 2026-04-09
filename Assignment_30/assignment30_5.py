import os

def main():
    existing_file = input("Enter the file name: ")
    value = input("Enter the word to find :")
    
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
        # Search for word in the file
        word_found = False
        with open(filepath, 'r') as file:
            for line in file:
                if value in line:
                    word_found = True
                    break
        
        if word_found:
            print(f"The word '{value}' exists in the file")
        else:
            print(f"The word '{value}' does not exist in the file")
        
    except Exception as e:
        print(f"Error: {e}")
  
if __name__ == "__main__":
    main()