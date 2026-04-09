import os
import sys

def main():
    if len(sys.argv) < 2:
        print("Usage: python assignment29_3.py <filename>")
        return
    
    filename = sys.argv[1]
    
    found = False
    filepath = None
    
    # Use walk method to find the file
    for root, dirs, files in os.walk('.'):
        if filename in files:
            found = True
            filepath = os.path.join(root, filename)
            print(f"File '{filename}' found in directory: {root}")
            break
    
    if not found:
        print(f"File '{filename}' does not exist")
        return
    
    try:
        # Read content from existing file
        with open(filepath, 'r') as source_file:
            contents = source_file.read()
        
        # Write content to demo.txt
        with open('demo.txt', 'w') as dest_file:
            dest_file.write(contents)
        
        print(f"Successfully copied contents from '{filename}' to 'demo.txt'")
        print(f"\n--- Contents copied ---")
        
    except Exception as e:
        print(f"Error: {e}")
  
if __name__ == "__main__":
    main()