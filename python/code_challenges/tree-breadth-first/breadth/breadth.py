class Node:
    def __init__(self,value):
        self.value = value
        self.next = None
        self.left = None
        self.right = None

class Queue:
    def __init__(self):
        self.front = None
        self.rear = None

    def enqueue(self,value):

        node = Node(value)
        if not self.front:
            self.front = node
            self.rear = node
        else:
            self.rear.next = node
            self.rear = node

    def dequeue(self):
        try:
           dequeueVal=self.front.value
           self.front=self.front.next
           return dequeueVal
        except:
           return 'The Queue is empty'

class BinaryTree:
    def __init__(self):
        self.root = None
        self.max = 0
        self.list =[]
    def preOrder(self):

        output =" "
        def traverse(node):
            output.append(node.value)

            if node.left:
                traverse(node.left)

            if node.right:
                traverse(node.right)

        traverse(self.root)
        return output

    def in_order(self):
        output = " "
        def traverse(node):

            if node.left:
                traverse(node.left)

            output.append(node.value)

            if node.right:
                traverse(node.right)

        traverse(self.root)
        return output

    def postOrder(self):
        output =" "

        def traverse(node):
            if node.left:
                traverse(node.left)
            if node.right:
                traverse(node.right)

            output.append(node.value)
        traverse(self.root)
        return output

    def find_max(self):

        def traverse(node):

            if node.left:
              traverse(node.left)

              if node.left.value>self.max:
                self.max=node.left.value

            if node.right:
              traverse(node.right)
              if node.right.value>self.max:
                self.max=node.right.value

        traverse(self.root)

        if self.root.value>self.max:
          return self.root.value

        return self.max

def breadth_first(tree):
        queue =[tree.root]
        breadth= []
        if tree.root==None:
            return[]
        while queue:
            node=queue[0]
            if node.left !=  None:
                queue +=[node.left]

            if node.right != None:
                queue +=[node.right]

            breadth +=[queue[0].value]
            queue=queue[1:]
        return breadth




if __name__ == "__main__":

    tree = BinaryTree()
    tree.root = Node(4)
    tree.root.left = Node(8)
    tree.root.right = Node(2)
    tree.root.left.left = Node(25)
    tree.root.left.right = Node(9)
    tree.root.left.right.left = Node(6)
    tree.root.left.right.right = Node(3)
    print(breadth_first(tree))
