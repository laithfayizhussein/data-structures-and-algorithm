class Node:

     def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None
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
   pass
