# create a list contains 20 random int between 1000 and 5000
import random

li = []
for i in range(20):
    li.append(random.randint(1000, 5000))
print(li)

ss = [2, 3, 5, 7]
for i in li:
    for j in ss:
        if i % j == 0:
            break
    else:
        print(i, end=' ')
