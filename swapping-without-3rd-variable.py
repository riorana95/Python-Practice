def inp():
    try:
        a = int(input("Enter 1st numeric value: "))
        b = int(input("Enter 2nd Numeric value: "))
        return a, b
    except:
        print("Only Numeric Value")
        print()
        return inp()

a,b = inp()
print("Before Swap a =",a)
print("Before Swap b =",b)
a = a + b
b = a - b
a = a - b
print()
print("After Swap a =",a)
print("After Swap b =",b)