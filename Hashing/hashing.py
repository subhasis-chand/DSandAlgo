def hashing(data, len):
    return data % len

def hashingstring(s, len):
    hash_value = 0
    p = 31  # A prime number
    p_pow = 1

    for char in s:
        hash_value = hash_value + ord(char)

    return hash_value

class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [[] for _ in range(size)]

    def insert(self, key, value):
        hash_index = hashing(key, self.size)
        for i, (k, v) in enumerate(self.table[hash_index]):
            if k == key:
                self.table[hash_index][i] = (key, value)
                return
        self.table[hash_index].append((key, value))

    def search(self, key):
        hash_index = hashing(key, self.size)
        for k, v in self.table[hash_index]:
            if k == key:
                return v
        return None

    def delete(self, key):
        hash_index = hashing(key, self.size)
        for i, (k, v) in enumerate(self.table[hash_index]):
            if k == key:
                del self.table[hash_index][i]
                return True
        return False

if __name__ == "__main__":
    data = 10
    len = 5
    print("Hash value:", hashing(data, len))