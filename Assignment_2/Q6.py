# Write a program that accepts two numbers from user and prints their :
# - Addition
# - Substration
# - Multiplication
# - Division

print("Enter two numbers : ")

n1 = int(input())
n2 = int(input())

def addition():
    add = None

    add = n1+n2

    return add

def multiplication ():
    mult = None

    mult = n1*n2

    return mult

def subtraction():
    sub = None
    sub = n1-n2
    return sub

def division():
    divi = None
    divi = n1/n2

    return divi

print("Addition is :", addition())
print("Subtraction is :", subtraction())
print("Multiplication is :", multiplication())
print("Division is :", division())