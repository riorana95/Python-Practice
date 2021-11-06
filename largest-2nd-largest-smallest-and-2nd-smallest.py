def inp():
    try:
        n = list(map(int,input("Enter array spacing b/w element:").split(" ")))
        return n
    except:
        print("Error! Numeric Value only")
        print()
        return inp()
        
x = inp() #[25, 10, 11, 45, 30]

s1 = l1 = x[0] #[25]
l2 = s2 = x[1] #[10]

for i in x:
    if l1 < i:
        l2 = l1
        l1 = i
        
    elif i < l1 and l2 < i:
        l2 = i
        
for i in x:
    if s1 > i:
        s2 = s1
        s1 = i
    
    elif i < s2 and  i != s1:
        s2 = i
    
print("largest is", l1, "and second largest is",l2)
print("smallest is", s1, "and second smallest is",s2)
