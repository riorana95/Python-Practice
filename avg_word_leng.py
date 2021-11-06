sent = "This : ; ?/ rio' average length of the word"
# word = 7; letter 29

for p in ":;?/'":
    sent = sent.replace(p,"")
words = sent.split()
add = 0
for letter in words:
    word_length = len(letter)
    add += word_length
avg = add / len(words)
print(avg)