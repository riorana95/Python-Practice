def inp():
    try:
        n = int(input("Enter Number:"))
        return n
    except:
        print("Enter Numeric value")
        print()
        return inp()

x = inp()

rem = x%10
if rem >= 5:
    add = 10 - rem
    multi_10 = x + add
else:
    sub = 10 - rem
    multi_10 = x - rem

print(multi_10)
    