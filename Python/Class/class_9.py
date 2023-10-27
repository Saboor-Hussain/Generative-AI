import sys

print("line 1")
print("line 2")

print(type(sys.argv))
print(sys.argv) # iterative datatype


# Compairing sys.argv arguments

# 0 - index always contain file name
if sys.argv[1] == "-g":
    print("I will install this package on globally in your system!")