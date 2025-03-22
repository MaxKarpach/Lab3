import random

file = open("input.txt", "w")

n = random.randint(1, 10**6)
file.write(str(n) + '\n')

for i in range(n):
    file.write(str(random.randint(1,10**9)) + ' ')

file.close()
