import math
import psutil
process = psutil.Process()
def is_perfect_square(n):
    s = int(math.isqrt(n))
    return s * s == n
def is_fibonacci_number(num):
    num = int(num)
    return is_perfect_square(5 * num * num + 4) or is_perfect_square(5 * num * num - 4)
c = open("input.txt").readline()
n = open("input.txt").readlines()[1:]
w = open("output.txt", "w")
for i in range(len(n)-1):
    if i != c:
        n[i] = n[i][:-1]
for i in range(len(n)):
    if (is_fibonacci_number(n[i])):
        w.write('Yes' + '\n')
    else:
        w.write('No' + '\n')
w.close()
print(process.memory_info().rss / 1024 / 1024)
