def checking(char):
    if char == 'a' or char == 'e' or char == 'i' or char == 'o' or char == 'u' or char == 'A' or char == 'E' or char == 'I' or char == 'O' or char == 'U':
        print(f"{char} is a vowel")
    else:
        print(f"{char} is a consonant")


def main():
    char = input("Enter a character: ")
    checking(char)
   
    
if __name__ == "__main__":
    main()
