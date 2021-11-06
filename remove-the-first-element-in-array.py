def inp():
    try:
        n = list(map(int,input("Enter Number spacing b/w each element ").split(" ")))
        return n
    except:
        print("Enter Numeric value")
        print()
        return inp()

x = inp()

x.pop(0)
    
print(x)