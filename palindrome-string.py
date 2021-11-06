x = input("Enter String:")

pal = ""
for i in range(len(x)-1,-1,-1):
    pal += x[i]

if x == pal:
    print(pal,"is palindrome")
else:
    print(pal,"is not palindrome")