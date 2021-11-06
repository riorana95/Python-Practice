# reverse integer
n = input("Enter the Integer Value:")
if n[0] == "-":
    a = '-'+n[:0:-1]
else:
    a = n[::-1]
print(int(a))