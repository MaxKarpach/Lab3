import random
buffer_size, n = random.randint(1, 10**5), random.randint(1, 10**5)

file = open("input.txt" , 'w')
file.write(str(buffer_size) + ' ' + str(n) + '\n')

time_check = 0
for i in range(n):
    time_check += random.randint(0, 10)
    file.write(str(time_check) + ' ' + str(random.randint(0, 10*3)) + '\n')

file.close()
