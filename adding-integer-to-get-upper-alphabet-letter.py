num = int(input())

# adding integer
def add(num):
    st = str(num)
    add = 0
    for i in st:
        add += int(i)
    return add

# checking integer value is greater than 26    
check = add(num)
while check > 26:
    check = add(check)

    
ch = 64+ check # adding value in check(variable) to get upper Alphabet
print(chr(ch))

    
