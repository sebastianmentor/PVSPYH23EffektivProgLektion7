from dataclasses import dataclass

def my_hash(data:str) -> int:
    return sum(ord(i) for i in data)

print(my_hash('abc'))

class HashItem:
    def __init__(self, hash_val, data) -> None:
        self.hash_val = hash_val
        self.data = data

    def __str__(self) -> str:
        return f"{self.hash_val} -> {self.data}"

    def __repr__(self) -> str:
        return f"HashItem({self.hash_val},{self.data})"

class HashTable:
    def __init__(self) -> None:
        self.size = 8
        self.table: list[HashItem] = [None] * self.size
        self.loadfactor = 0.75
        self.current = 0

    def _grow_table(self) -> None:
        self.size *= 2
        self.current = 0
        print('Vi växer', self.size)
        table = self.table
        self.table = [None] * self.size

        for item in table:
            if item:
                self.append(item.hash_val, item.data)


    def append(self, hash_val, data):
        hash_item = HashItem(hash_val=hash_val, data=data)

        _hash = my_hash(hash_val) % (self.size)

        while True:
            if self.table[_hash]:
                if self.table[_hash].hash_val == hash_val:
                    break
                _hash += 1 
                _hash = _hash % (self.size)
            else:
                break

        if not self.table[_hash]:
            self.current += 1

        self.table[_hash] = hash_item
        if self.load():
            self._grow_table()

    def get_item(self, hash_val) -> HashItem|None:

        _hash = my_hash(hash_val) % (self.size)
        
        while self.table[_hash]:

            if self.table[_hash].hash_val == hash_val:
                return self.table[_hash].data
            
            print(_hash)
            _hash = (_hash + 1) % (self.size)

        return None

    def load(self) -> bool:
        return (self.current/self.size) > self.loadfactor 

    def print_table(self):
        print(self.table)
        print(len(self.table))

table = HashTable()

table.append('abc', 'Secret')
table.append('abd', 'Secret2')
table.append('cba', 'Secret3')
table.append('abc', 'New Secret')

print(table.get_item('abc'))
print(table.get_item('Hello'))

table.print_table()

print("#"*22)

table.append('aberfr', 'asdfasdffsda')
table.append('84844848', 'lskdafljs')
table.append('99494kd', 'sdaflses')
table.append('99525993', 'New Secret 333')
table.append('99523', 'New Secret 333')
table.append('1111', 'New Secret 333')


table.print_table()

