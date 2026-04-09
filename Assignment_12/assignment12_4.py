
def cubeNum(value1):
    return value1 * value1 * value1
    

def main():
    no =int(input("Enter first number: "))


    result = cubeNum(no)
    print("Cube is :", result)
    
if __name__ == "__main__":
    main()