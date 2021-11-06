def inp():
    try:
        n = list(map(int,input("Enter array spacing b/w element:").split(" ")))
        return n
    except:
        print("Error! Numeric Value only")
        print()
        return inp()
        
x = inp()

add = 0
for i in x:
    add += i
    
print("Sum of element in a array:",add)