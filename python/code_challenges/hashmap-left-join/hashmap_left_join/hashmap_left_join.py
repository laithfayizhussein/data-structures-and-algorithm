class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def add(self, data):
        node = Node(data)
        if not self.head:
            self.head = node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = node
    def __str__(self):
        values = []
        current = self.head
        while current:
            values.append(current.data)
            current = current.next
        return f'{values}'
    
class Hash_table:
    def __init__(self, size=1024):
        self.size = size
        self.map = [None]*size

    def hash(self, key):
        ascii = 0
        for ch in key:
            ascii_ch = ord(ch)
            ascii += ascii_ch
        temp_value = ascii * 19
        hashed_key = temp_value % self.size
        return hashed_key

    def add(self, key, value):
        hashed_key = self.hash(key)
        if not self.map[hashed_key]:
            self.map[hashed_key] = LinkedList()
        self.map[hashed_key].add((key,value))

    def contains(self,key):
        hashed_key = self.hash(key)
        if self.map[hashed_key]:
            self.map[hashed_key].head.data[0]
            current=self.map[hashed_key].head
            while current:
                if current.data[0]==key:
                    return True
                else:
                    current=current.next
        return False

    def get(self,key):
        hashed_key = self.hash(key)
        if self.map[hashed_key]:
            self.map[hashed_key].head.data[0]
            current=self.map[hashed_key].head
            while current:
                if current.data[0]==key:
                    return current.data[1]
                else:
                    current=current.next
        return None

def left_join(hash1,hash2):
    array=[]
    if hash1.map == hash1.size*[None] or hash2.map == hash2.size*[None] :
        return 'hash table is empty'
    for item in hash1.map:
        if item:
            array2=[]
            array2.append(item.head.data[0])
            array2.append(hash1.get(item.head.data[0]))
            array2.append(hash2.get(item.head.data[0]))
            array.append(array2)
    return array


if __name__ == "__main__":
  pass
