i_file = open("input.txt", 'r')
n = int(i_file.readline())
numbers = list(map(int, i_file.readline().split()))
i_file.close()

checker = True
for i in range(n):
    if 2*i <= n-1:
        if numbers[i] <= numbers[2*i]:
            if 2*i+1 <= n-1:
                if numbers[i] > numbers[2*i+1]:
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
