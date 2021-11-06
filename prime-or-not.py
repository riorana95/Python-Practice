def inp():
    try:
        p = int(input("Enter 1st numeric value: "))
        return p
    except:
        print("Only Numeric Value")
        print()
        return inp()

n = inp()

c = 0
for i in range(1,n+1):
    if n%i == 0:
        c += 1

print(c)
if c == 2:
    print(n,"is prime")
else:
    print(n,"is not prime")