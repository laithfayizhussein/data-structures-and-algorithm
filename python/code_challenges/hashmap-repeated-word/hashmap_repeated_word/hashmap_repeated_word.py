import re
class Node:
    def __init__(self, data):
        self.data=data
        self.next=None

class LinkedList:
    def __init__(self):
        self.head=None

    def add(self, data):
        node=Node(data)
        if not self.head:
            self.head=node
        else:
            current=self.head
            while current.next:
                current=current.next
            current.next=node

    def __str__(self):
        values =[]
        current = self.head
        while current:
            values.append(current.data)
            current = current.next
        return f'{values}'

class Hash_table:
    def __init__(self, size):
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

    def add(self,key,value):

        hashed_key = self.hash(key)
        if not self.map[hashed_key]:
            self.map[hashed_key] = LinkedList()
        self.map[hashed_key].add((key,value))

    def contains(self,key):

        hashed_key=self.hash(key)
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
        if self.map [hashed_key]:
            self.map [hashed_key].head.data[0]
            current=self.map[hashed_key].head
            while current:
                if current.data[0]== key:
                    return current.data[1]
                else:
                    current=current.next
        return None
def repeated_word(book=None):
    if book==None:
        return 'book is empty'
    hash_table=Hash_table(1024)

    book =re.sub('\W+', ' ',book).lower().split()

    for word in book:

        if hash_table.contains(word):
            return word
        else:
            hash_table.add(word, True)

