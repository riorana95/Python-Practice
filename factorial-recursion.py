# Recursion
# Factorial

def inp():
    try:
        n = int(input("Enter number: "))
        return n
    except:
        print("Error! Numeric Value only")
        print()
        return inp()

def fact(x):
    if x == 1:
        return 1
    return x * fact(x-1)
    

a = fact(inp())
print(a)