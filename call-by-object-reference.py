# Topic “Call by Object Reference”

def inp():
    try:    
        n = int(input("Enter value: "))
        return n
    except:
        print("Error! Numeric Value only")
        print()
        return inp()
        
# Taking index input
def ind_value():
    try:    
        n = int(input(f"Enter Index 0 to {len_list-1} Value to update: "))
        return n
    except:
        print("Error! Length of index  should be in numeric Value only")
        print()
        return ind_value()

#Taking list value
def my_list():
    try:    
        n = list(map(int, input("Enter list value by spacing between the number:\n").split()))
        return n
    except:
        print("Error! List Should be in numeric value only")
        print()
        return my_list()

mylist = my_list()
print(mylist)
len_list = len(mylist) #length of list

# Object Reference example
def update(mylist):
    index_val = ind_value()
    try:
        mylist[index_val] = inp()
        print("Inside Function",mylist)
    except IndexError:
        print(f"Error! List out of Range, value should be between 0 to {len_list-1}")

update(mylist)
print("Outside Function",mylist)


'''
call by object Reference
def update(mylist):
    mylist[1] = 5
    print("Inside Function", mylist)
 
# Driver's code
mylist = [10,20,30,40]
 
update(mylist)
print("Outside Function:", mylist)
'''