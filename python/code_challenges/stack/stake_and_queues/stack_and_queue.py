class ErrorOperator(BaseException):
    pass

class Node():
    def __init__(self, value, next=None):
        self.value =value
        self.next =next

class Stack():
    """
    first in last out  FILO
    """
    def __init__(self, node=None):
        self.top = node


    def push(self, value):

        node = Node(value)
        node.next = self.top
        self.top = node

    def pop(self):

        if self.is_empty():
            raise ErrorOperator(" an empty collection")

        item = self.top
        self.top = self.top.next
        item.next = None
        return item.value

    def peek(self):
        if self.is_empty():
            raise ErrorOperator("an empty collection")
        return self.top.value

    def is_empty(self):

        if self.top == None:
            return True
        else:
            return False


class Queue():

    """
   first in first out FIFO
    """
    def __init__(self):
        self.front = None
        self.rear = None  #rear points to the last element in the queue

    def enqueue(self, value):

        node = Node(value)
        if not self.rear:
            self.front = node
            self.rear = node
        else:
            self.rear.next = node
            self.rear = node
    def dequeue(self):

        if self.is_empty():
            raise ErrorOperator("an empty collection")

        item = self.front
        self.front = self.front.next
        item.next = None

        return item.value

    def is_empty(self):

        if self.front == None:
            return True

    def peek(self):
        if self.is_empty():
            raise ErrorOperator("an empty collection")
        return self.front.value

    #resorse https://www.techiedelight.com/queue-implementation-python/
