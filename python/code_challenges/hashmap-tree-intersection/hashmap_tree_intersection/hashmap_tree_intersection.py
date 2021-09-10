class Node:
    def __init__(self, data ,):
        self.data = data
        self.next= None

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
    def __init__(self, size):
        self.size=size
        self.map=[None]*size

    def hash(self, key):
        sum_of_asccii = 0
        for ch in key:
            asccii_of_ch = ord(ch)
            sum_of_asccii += asccii_of_ch
        temp_value = sum_of_asccii * 19
        hashed_key = temp_value % self.size
        return hashed_key

    def add(self, key, value):
        hashed_key = self.hash(key)
        if not self.map[hashed_key]:
            self.map[hashed_key]=LinkedList()
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

class Node2:
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None

def intersection(f_tree,s_tree):
    arr=[]
    hashtable=Hash_table(1024)
    if f_tree.root==None or s_tree.root==None:
        return 'theres emptry tree'
    def _walk(node):
        if hashtable.contains(str(node.value)):
            nonlocal arr
            arr+=[node.value]
        else:
            hashtable.add(str(node.value),True)

        if node.left:
            _walk(node.left)
        if node.right:
            _walk(node.right)
    _walk(f_tree.root)
    _walk(s_tree.root)
    return arr



if __name__ == "__main__":
    f_tree=BinaryTree()
    f_tree.root=Node2(150)
    f_tree.root.left=Node2(100)
    f_tree.root.right=Node2(250)
    f_tree.root.left.left=Node2(75)
    f_tree.root.left.right=Node2(160)
    f_tree.root.right.left=Node2(200)
    f_tree.root.right.right=Node2(350)
    f_tree.root.left.right.left=Node2(125)
    f_tree.root.left.right.right=Node2(175)
    f_tree.root.right.right.left=Node2(300)
    f_tree.root.right.right.right=Node2(500)

    s_tree=BinaryTree()
    s_tree.root=Node2(42)
    s_tree.root.left=Node2(100)
    s_tree.root.right=Node2(600)
    s_tree.root.left.left=Node2(15)
    s_tree.root.left.right=Node2(160)
    s_tree.root.right.left=Node2(200)
    s_tree.root.right.right=Node2(350)
    s_tree.root.left.right.left=Node2(125)
    s_tree.root.left.right.right=Node2(175)
    s_tree.root.right.right.left=Node2(4)
    s_tree.root.right.right.right=Node2(500)

    print(intersection(f_tree,s_tree))


