class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

class HashTable:
    def __init__(self, initial_capacity=8, load_factor_threshold=0.75):
        self.capacity = initial_capacity
        self.size = 0
        self.load_factor_threshold = load_factor_threshold
        self.buckets = [None] * self.capacity

    def hash_function(self, key):
        """En enkel hash-funktion baserad på inbyggd hash()."""
        return hash(key) % self.capacity

    def insert(self, key, value):
        """Lägger till eller uppdaterar ett värde i hash-tabellen."""
        index = self.hash_function(key)
        new_node = Node(key, value)

        # Kolla om det redan finns en nod på den här indexplatsen
        current = self.buckets[index]
        if current is None:
            self.buckets[index] = new_node
            self.size += 1
        else:
            # Hantera kollision via länkad lista (chaining)
            prev = None
            while current:
                if current.key == key:
                    current.value = value  # Uppdatera om nyckeln redan finns
                    return
                prev = current
                current = current.next
            prev.next = new_node
            self.size += 1

        # Kolla om vi måste göra en rehashing baserat på belastningsfaktorn
        if self.size / self.capacity > self.load_factor_threshold:
            self.rehash()

    def rehash(self):
        """Gör omallokering av hash-tabellen när belastningen blir för hög."""
        print("Rehashing...")
        old_buckets = self.buckets
        self.capacity *= 2  # Dubblar kapaciteten
        self.buckets = [None] * self.capacity
        self.size = 0

        for node in old_buckets:
            while node:
                self.insert(node.key, node.value)
                node = node.next

    def search(self, key):
        """Hittar ett värde baserat på en nyckel."""
        index = self.hash_function(key)
        current = self.buckets[index]

        while current:
            if current.key == key:
                return current.value
            current = current.next

        return None

    def delete(self, key):
        """Tar bort ett värde baserat på en nyckel."""
        index = self.hash_function(key)
        current = self.buckets[index]
        prev = None

        while current:
            if current.key == key:
                if prev is None:
                    self.buckets[index] = current.next
                else:
                    prev.next = current.next
                self.size -= 1
                return True
            prev = current
            current = current.next

        return False

    def display(self):
        """Visar hash-tabellen på ett enkelt sätt."""
        for i, node in enumerate(self.buckets):
            if node:
                chain = []
                current = node
                while current:
                    chain.append(f"{current.key}: {current.value}")
                    current = current.next
                print(f"Index {i}: " + " -> ".join(chain))
            else:
                print(f"Index {i}: None")

# Exempel på användning
hash_table = HashTable()

hash_table.insert("apple", 5)
hash_table.insert("banana", 3)
hash_table.insert("orange", 10)

print("Innan rehash:")
hash_table.display()

hash_table.insert("pear", 7)
hash_table.insert("melon", 8)
hash_table.insert("grape", 4)

print("\nEfter rehash:")
hash_table.display()

# Sök efter värden
print("\nSök efter apple:", hash_table.search("apple"))
print("Sök efter grape:", hash_table.search("grape"))

# Ta bort ett element
hash_table.delete("banana")
print("\nEfter att ha tagit bort 'banana':")
hash_table.display()
