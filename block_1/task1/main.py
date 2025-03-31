i_file = open("input.txt", 'r')
n = int(i_file.readline())
numbers = list(map(int, i_file.readline().split()))
i_file.close()

checker = True
for i in range(1, n+1):
    if 2*i <= n:
        if numbers[i-1] <= numbers[2*i-1]:
            if 2*i+1 <= n:
                if numbers[i-1] > numbers[2*i]:
                    checker = False
                    break
        else:
            checker = False
            break
    else:
        break

o_file = open("output.txt", 'w')
if checker is True: o_file.write("YES")
else: o_file.write("NO")
o_file.close()
