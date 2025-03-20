class HashSet:
    def __init__(self, size=100):
        self.size = size
        self.table = [[] for _ in range(size)]

    def _hash(self, key):
        return hash(key) % self.size

    def insert(self, key):
        index = self._hash(key)
        if key not in self.table[index]:
            self.table[index].append(key)

    def remove(self, key):
        index = self._hash(key)
        if key in self.table[index]:
            self.table[index].remove(key)

    def exists(self, key):
        index = self._hash(key)
        return key in self.table[index]
set = HashSet()
c = open("input.txt").readline()
a = open("input.txt").readlines()[1:]
f = []
for i in range(len(a)):
    if a[i][0] == 'A':
        set.insert(a[i][2])
    elif a[i][0] == '?':
        f.append(set.exists(a[i][2]))
    elif a[i][0] == 'D':
        set.remove(a[i][2])
o = open("output.txt", "w")
for i in range(len(f)):
    if f[i] == True:
        o.write('Y' + '\n')
    else:
        o.write('N' + '\n')
o.close()

