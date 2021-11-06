# “Call by assignment”
def inp():
    try:
        n = int(input("Enter Value: "))
        return n
    except:
        print("Only Numeric Value only")
        print()
        return inp()

x = inp()

def update(x):
    x = inp()
    print("Inside fucntion",x)

update(x)
print("Outside Function",x)
    
