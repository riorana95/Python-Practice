def inp():
    try:
        num = int(input("Enter Numeric value: "))
        return num
    except:
        print("Enter Numeric Value only")
        print()
        return inp()
        
n = inp()

rev = 0
while n>0:
    r = n%10
    rev = rev * 10 + r
    n=n//10

print(rev)

    