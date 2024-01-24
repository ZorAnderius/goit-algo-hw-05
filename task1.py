class HashTable:
    def __init__(self, size: int):
        self.size = size
        self.table = [[] for _ in range(self.size)]

    def hash_function(self, key) -> int:
        return hash(key) % self.size

    def insert(self, key: int, value: int) -> bool:
        key_hash = self.hash_function(key)
        key_value = [key, value]
        
        if self.table[key_hash] is None:
            self.table[key_hash] = list([key_value])
            return True
        else:
            for pair in self.table[key_hash]:
                if pair[0] == key:
                    pair[1] = value
                    return True
            self.table[key_hash].append(key_value)
            return True

    def get(self, key: int) -> int or None:
        key_hash = self.hash_function(key)
        if self.table[key_hash] is not None:
            for pair in self.table[key_hash]:
                if pair[0] == key:
                    return pair[1]
        return None

    def delete(self, key: int) -> bool:
        key_hash = self.hash_function(key)
        if self.table[key_hash] is not None:
            index_delete = None
            for index in range(len(self.table[key_hash])):
                if self.table[key_hash][index][0] == key:
                    index_delete = index
                    break
            if index_delete is not None:
                self.table[key_hash].pop(index_delete)
                return True
        return False

def task1():
    H = HashTable(5)
    H.insert("apple", 10)
    H.insert("orange", 20)
    H.insert("banana", 30)


    print(H.get("apple"))   # Виведе: 10
    print(H.get("orange"))  # Виведе: 20
    print(H.get("banana"))  # Виведе: 30

    print(H.table)
    H.delete("orange")
    print(H.table)
    

if __name__ == '__main__':
    task1()