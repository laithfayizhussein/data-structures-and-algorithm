class Node:

     def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None
        self.max = 0

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



#other way to loop and find the max value
#geeksforgeeks.org/find-the-node-with-maximum-value-in-a-binary-search-tree/
# def find_maximum(root):
#     current = root

#     #loop down to find the rightmost leaf
#     while(current.right):
#         current = current.right
#     return current.data

class BinarySearchTree(BinaryTree):
    def add(self,value):
        if not self.root:
            self.root = Node(value)

        else:
            def traverse(node):
                # lift for min num
                if value < node.value:
                    if not node.left:
                        node.left = Node(value)
                        return
                    else:
                        traverse(node.left)

                # right for max num
                else:
                    if not node.right:
                        node.right = Node(value)
                        return
                    else:
                        traverse(node.right)
            traverse(self.root)


    def empty_tree(self,value):

        # if there is not root // empty tree
        if not self.root:
            return False
        else:
            def traverse(node):
                # check the root value
                if value == node.value:
                    return True
                # lift for min num
                if value < node.value:
                    if node.left:
                        return traverse(node.left)
                    else:
                        return False
                # right for max num
                else:
                    if node.right:
                        return traverse(node.right)
                    else:
                        return False
            return traverse(self.root)

if __name__ == "__main__":
    tree = BinaryTree()
    tree.root = Node(55)
    tree.root.left = Node(23)
    tree.root.right = Node(44)
    tree.root.left.left = Node(3)
    tree.root.left.right = Node(7)
    tree.root.left.right.left = Node(77)
    tree.root.left.right.right = Node(11)
    tree.root.right.right = Node(32)
    tree.root.right.right.left = Node(1)

    print(tree.find_max())
