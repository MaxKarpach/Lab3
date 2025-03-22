i_file = open("input.txt", 'r')
info = list(map(int, i_file.readline().split()))
buffer_size = info[0]
n = info[1]

last_time = 0
buffer = []
rejected=[]
o_file = open("output.txt", 'w')

for i in range(n):
    paket = list(map(int, i_file.readline().split()))

    while buffer and last_time < paket[0] or buffer and buffer[0] == 0:
        while 0 in rejected:
            o_file.write('-1\n')
            rejected.remove(rejected[0])
        rejected = list(map(lambda x: x - 1, rejected))

        dif_time = paket[0] - last_time
        if buffer[0] <= dif_time:
            last_time += buffer[0]
            buffer.remove(buffer[0])
            if buffer: o_file.write(str(last_time) + '\n')
        else:
            buffer[0] -= dif_time
            last_time += dif_time

    if len(buffer) < buffer_size:
        if not buffer: o_file.write(str(paket[0]) + '\n')
        buffer.append(paket[1])
    else:
        rejected.append(buffer_size-1)

while buffer or rejected:
    while 0 in rejected:
        o_file.write('-1\n')
        rejected.remove(rejected[0])
    rejected = list(map(lambda x: x-1, rejected))

    if buffer:
        last_time += buffer[0]
        buffer.remove(buffer[0])
        if buffer: o_file.write(str(last_time) + '\n')


o_file.close()
i_file.close()
