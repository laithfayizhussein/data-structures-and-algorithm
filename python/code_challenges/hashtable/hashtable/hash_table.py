class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
class LinkedList:
    def __init__(self):
        self.head = None

    def add(self, value):
        node = Node(value)
        if not self.head:
            self.head = node
        else:
            current = self.head
            while current.next:
                current = current.next

            current.next = node
    def __str__(self):
        list_val = []
        current = self.head
        while current:
            list_val.append(current.value)
            current = current.next
        return f'{list_val}'
class Hashtable:
    def __init__(self, size):
        self.size= size
        self.map= [None]*size

    def hash(self, key):
        ascii= 0
        for ch in key:
            ascii_ch= ord(ch)
            ascii+= ascii_ch
        temp_value= ascii * 19
        hashed_key= temp_value % self.size
        return hashed_key

    def add(self, key, value):
        hashed_key =self.hash(key)
        if not self.map[hashed_key]:
            self.map[hashed_key] =LinkedList()
        self.map[hashed_key].add((key,value))

    def contains(self,key):
        hashed_key = self.hash(key)
        if self.map[hashed_key]:
            self.map[hashed_key].head.value[0]
            current=self.map[hashed_key].head
            while current:
                if current.value[0] == key:
                    return True
                else:
                    current=current.next
        return False

    def get(self,key):
        hashed_key= self.hash(key)
        if self.map[hashed_key]:
            self.map[hashed_key].head.value[0]
            current= self.map[hashed_key].head
            while current:
                if current.value[0] ==key :
                    return current.value[1]
                else:
                    current=current.next
        return None

