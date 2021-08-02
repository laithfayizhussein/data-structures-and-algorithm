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
    def insertBefore(self ,value, newVal):


        current = self.head
        if current.value==value:
            self.insert(newVal)
        else:
          while current:

             if current.next.value==value :
                nextvalue=current.next
                current.next=Node(newVal)
                current.next.next=nextvalue
                break
             current=current.next


    def insertAfter(self, value, newVal):


        current = self.head
        while current:
            if current.value==value :
                nextvalue=current.next
                current.next=Node(newVal)
                current.next.next=nextvalue
                break
            current=current.next


    def kthFromEnd(self, k):

        current = self.head
        length = 0

        if k < 0:
            return 'not a positive number has been entered'

        while current is not None:
            current = current.next
            length += 1

        if k >length:
            return 'Number is greater than the end of the list'

        current =self.head
        for i in range(0, length - k):
            current =current.next
        return current.value


    def __str__(self):

        output = ""
        current =self.head
        while current:
            value =current.value
            if current.next is None:
                output +=f"( {value} ) -> null"
                break
            output =output + f"( {value} ) -> "
            current=current.next
        return output


if __name__ == "__main__":
 pass
