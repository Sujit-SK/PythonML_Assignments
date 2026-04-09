import os
import sys

def main():
    if len(sys.argv) < 3:
        print("Usage: python assignment29_4.py <file1> <file2>")
        return
    
    filename1 = sys.argv[1]
    filename2 = sys.argv[2]
    
    # Use walk method to find both files
    filepath1 = None
    filepath2 = None
    
    for root, dirs, files in os.walk('.'):
        if filename1 in files and filepath1 is None:
            filepath1 = os.path.join(root, filename1)
        if filename2 in files and filepath2 is None:
            filepath2 = os.path.join(root, filename2)
        if filepath1 and filepath2:
            break
    
    # Check if both files were found
    if not filepath1:
        print(f"File '{filename1}' does not exist")
        return
    
    if not filepath2:
        print(f"File '{filename2}' does not exist")
        return
    
    print(f"Found '{filename1}' at: {filepath1}")
    print(f"Found '{filename2}' at: {filepath2}")
    
    try:
        # Read content from first file
        with open(filepath1, 'r') as file1:
            contents1 = file1.read()
        
        # Read content from second file
        with open(filepath2, 'r') as file2:
            contents2 = file2.read()
        
        # Compare contents
        if contents1 == contents2:
            print("SUCCESS: Both files have the same content")
            
        else:
            print("FAILURE: Files have different content")
          
        
    except Exception as e:
        print(f"Error: {e}")
        return False
  
if __name__ == "__main__":
    main()