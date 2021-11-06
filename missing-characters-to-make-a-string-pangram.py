x = input("Enter String:")

char = []
mx_char = 26
for i in range(mx_char):
    if chr(97+i) not in x:
        char.append(chr(97+i))
        
print(char)