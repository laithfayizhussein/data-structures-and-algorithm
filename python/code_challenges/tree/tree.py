class Node:

     def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
  # i will use the queue it self without import just for practice
class Queue:
    def __init__(self):
        self.front = None
        self.rear = None

    def enqueue(self,data):
        node =Node(data)

        if self.rear:
            self.rear.next = node
            self.rear = node
        else:
            self.front = node
            self.rear = node

    def dequeue(self):
        temp = self.front
        if self.is_empty():
            raise AttributeError ('Queue is empty')

        else:
            self.front = self.front.next
            temp.next= None
        if self.front ==None:
            self.rear = None
        return temp.value



class BinaryTree:

    def __init__(self):
        self.root = None








