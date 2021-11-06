def inp():
    try:
        n = int(input("Enter Number:"))
        return n
    except:
        print("Enter Numeric value")
        print()
        return inp()

x = inp()
num = x
pal = 0

while num > 0:
    rem = num % 10
    pal = pal * 10 + rem
    num = num//10

if pal == x:
    print(x,"is palindrome")
else:
    print(x,"is not palindrome")