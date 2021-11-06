def inp():
    try:
        n = int(input("Enter numeric Value: "))
        return n
    except:
        print("Enter Numeric Value only")
        print()
        inp()

x = inp()
for i in range(x,0,-1):
    for j in range(i):
        print(j+1,end="")
    print()