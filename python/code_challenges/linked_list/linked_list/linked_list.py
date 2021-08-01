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



    def append(self, value='null'):

        try:
          node = Node(value)
          if not self.head:
              self.head = node

          else:
              current = self.head
              while current.next != None:
                  current = current.next
              current.next = node
        except Exception as e:
          raise Exception(f"Something's Going Wrong:{e}")


    def includes(self,number):
        try:
          val=False

          current = self.head
          while current:
              if current.value==number:

                  val=True
                  break
              current=current.next
          return val
        except Exception as q:
          raise Exception(f" Error acourding :{q}")

          "add new value befor the head node "
    def insert_before(self, value, new_value):

        current = self.head
        if current.value==value:
            self.insert(new_value)
        else:
         while current:

             if current.next.value==value :
                nextvalue=current.next
                current.next=Node(new_value)
                current.next.next=nextvalue
                break
             current=current.next


    def insert_after(self, value, new_value):

          new_node = Node(new_value)
          current = self.head

          if current is None:
            self.insert_node(new_node)
            return

          while current is not None:
            if current.value == value:
                new_node.next = current.next
                current.next = new_node
            current = current.next
            return


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
 pass
