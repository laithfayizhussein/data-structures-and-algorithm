from linked_list import (
    LinkedList ,
   
)

def zip_ll(ll1, ll2):
    current1 = ll1.head
    current2 = ll2.head

    if current1 == None or current2 == None:
        if current1:
            return ll1.__str__()
        elif current2:
            return ll2.__str__()
        else:
         return " the linked list both empty"

    vlist = []
    while current1 or current2:
        if(current1):
            vlist+=[current1.value]
            current1 = current1.next
        if(current2):
            vlist+=[current2.value]
            current2 = current2.next
    new=''
    for i in vlist:
      new+=f'( {i} ) -> '
    new+='None'
    return new

#test both linked list

if __name__ == "__main__":
    ll1 = LinkedList()
    ll1.append(1)
    ll1.append(3)
    ll1.append(5)
    ll1.append(7)
    ll2 = LinkedList()
    ll2.append(2)
    ll2.append(4)
    ll2.append(6)

    print(ll1.__str__())
    print(ll2.__str__())
    print(zip_ll(ll1, ll2))


