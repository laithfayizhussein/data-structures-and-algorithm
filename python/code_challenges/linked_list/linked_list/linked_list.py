class Node:

    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, value='null'):

        try:
          node = Node(value)
          if not self.head:
              self.head = node
          else:
              current = self.head
              self.head= node
              self.head.next=current
        except Exception as q:
          raise Exception(f"Error acourding  : {q}")



    def includes(self,number):
        try:
          s=False

          current = self.head
          while current:
              if current.value==number:

                  s=True
                  break
              current=current.next
          return s
        except Exception as q:
          raise Exception(f" Error acourding  : {q}")

    def __str__(self):

        output = ""
        current = self.head
        while current:
            value = current.value
            if current.next is None:
                output += f"( {value} ) -> null"
                break
            output = output + f"( {value} ) -> "
            current=current.next
        return output

if __name__ == "__main__":

    ll = LinkedList()


    ll.insert(9)
    ll.insert(6)
    ll.insert(10)
    print(ll.__str__())


