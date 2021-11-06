def inp():
    try:
        n = int(input("Enter Year: "))
        return n
    except:
        print("Enter Numeric value")
        print()
        return inp()

x = inp()

if (x % 4 == 0) and (x % 400 == 0 or x % 100 != 0):
    print(x,"is leap year")
else:
    print(x,"not leap year")