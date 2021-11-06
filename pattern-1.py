def inp():
    try:
        n= int(input("Enter Numeric Value: "))
        return n
    except:
        print("Enter numeric value only")
        print()
        inp()

x = inp()

for i in range(x,0,-1):
    for j in range(i):
        print("*",end="")
    print()
