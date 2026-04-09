import os

def main():
    filename = input("Enter the file name: ")
    search_string = input("Enter the string to search: ")
    
    # Check if file exists
    if not os.path.isfile(filename):
        print(f"File '{filename}' does not exist")
        return
    
    try:
        # Read content from file
        with open(filename, 'r') as file:
            contents = file.read()
        
        # Count frequency of the string manually
        frequency = 0
        search_len = len(search_string)
        content_len = len(contents)
        print(content_len)
        for i in range(content_len - search_len + 1):
            if contents[i:i + search_len] == search_string:
                frequency += 1
        
        print(f"The string '{search_string}' appears {frequency} times in the file '{filename}'")
        
    except Exception as e:
        print(f"Error: {e}")
  
if __name__ == "__main__":
    main()