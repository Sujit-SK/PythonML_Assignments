import sys
# write a program to display:

# Data type
# Memory address
# Size in bytes of a variable entered by the user.
# Ans:

name = "Mayur"

print("Data Type :", type(name))
print("Memory Address :", id(name))
print("Size is bytes :", sys.getsizeof(name))
