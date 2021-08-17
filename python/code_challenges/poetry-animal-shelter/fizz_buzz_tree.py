class Node:
    def __init__(self,value):
        self.value=value
        self.children= []

class K_AryTree:
    def __init__(self):
        self.root= None

def fizz_buzz_tree(k_AryTree):
    def _walk(node):
        if node.children:
            for i in range(len(node.children)):
                _walk(node.children[i])
                if node.children[i].value %5==0 and node.children[i].value %3==0:
                   node.children[i].value='Fizz Buzz'

                elif node.children[i].value %5==0:
                     node.children[i].value='Buzz'

                elif node.children[i].value %3==0:
                     node.children[i].value='Fizz'
                else:
                    node.children[i].value=str(node.children[i].value)
    _walk(k_AryTree.root)

    if k_AryTree.root.value %5==0 and k_AryTree.root.value %3==0:
       k_AryTree.root.value='Fizz Buzz'

    elif k_AryTree.root.value %5==0:
         k_AryTree.root.value='Buzz'

    elif k_AryTree.root.value %3==0:
        k_AryTree.root.value='Fizz'

    else:
        k_AryTree.root.value=str(k_AryTree.root.value)

    return k_AryTree

if __name__ == "__main__":
    pass 
