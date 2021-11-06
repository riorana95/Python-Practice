from collections import Counter

z = [2,4,5,5,4,4]

di = Counter(z)
print(di)

key_max = max(di.keys(), key=(lambda k: di[k]))
key_min = min(di.keys(), key=(lambda k: di[k]))

print(key_max, key_min)

diff = di[key_max] - di[key_min]

print(diff)