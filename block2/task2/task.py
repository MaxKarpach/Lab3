class HashTable:
    def __init__(self, m):
        self.m = m  # Количество сегментов (карманов)
        self.p = 1000000007  # Простое число
        self.x = 263  # Константа для полиномиального хеширования
        self.table = [[] for _ in range(m)]

    def _hash_function(self, s):
        hash_value = 0
        for char in reversed(s):
            hash_value = (hash_value * self.x + ord(char)) % self.p
        return hash_value % self.m

    def add(self, string):
        index = self._hash_function(string)
        if string not in self.table[index]:
            self.table[index].insert(0, string)  # Вставляем в начало списка

    def delete(self, string):
        index = self._hash_function(string)
        if string in self.table[index]:
            self.table[index].remove(string)

    def find(self, string):
        index = self._hash_function(string)
        return "yes" if string in self.table[index] else "no"

    def check(self, i):
        return " ".join(self.table[i])


with open("input.txt", "r") as f:
    m = int(f.readline().strip())
    n = int(f.readline().strip())
    hash_table = HashTable(m)
    result = []

    for _ in range(n):
        query = f.readline().strip().split()
        command, value = query[0], query[1] if len(query) > 1 else None

        if command == "add":
            hash_table.add(value)
        elif command == "del":
            hash_table.delete(value)
        elif command == "find":
            result.append(hash_table.find(value))
        elif command == "check":
            result.append(hash_table.check(int(value)))

with open("output.txt", "w") as f:
    f.write("\n".join(result) + "\n")
