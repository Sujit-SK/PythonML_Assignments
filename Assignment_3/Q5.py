# what is difference between :
# - print
# - return

#print
# Ans - print key word is use to display instruction
#  to user or display result.
# Example :

print("Enter your name : ")


#return
# Ans - return key word is use to return out put 
# of function.
# Example :


name = input()

def displayname():
    ret = "Hello, "+name
    return ret

print(displayname())