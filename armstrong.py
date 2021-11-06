def inp():
    try:
        n = int(input("Enter Year: "))
        return n
    except:
        print("Enter Numeric value")
        print()
        return inp()

x = inp()

len_num = len(str(x))
num = x
arm = 0
while num > 0:
    rem = num%10
    arm = arm + rem ** len_num
    num = num//10
    
if arm == x:
    print(x, "is armstrong number")
else:
    print(x,"is not armstrong")
    
    
