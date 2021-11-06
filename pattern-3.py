def inp():
    try:
        n = int(input("Enter Numeric value: "))
        return n
    except:
        print("Enter Numeric Value only")
        print()
        return inp()
        
x = inp()
l = x//2
s = x
print(s)
for i in range(x,l,-1):
    for j in range(i,l+1,-1):
        print(s," ",end="")
        s = s - 1
    print()
