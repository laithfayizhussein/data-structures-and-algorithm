from linked_list import LinkedList


def zip_linked_list(ll1,ll2):
    """
    * form the tow list it will return one
    """
    if not ll1:
        return ll2
    if not ll2:
        return ll1
    the_result = LinkedList()
    current1 = ll1.head
    current2 = ll2.head
    while current1:
        the_result.append(current1.value)
        if  current2:
            the_result.append(current2.value)
            current2 = current2.next
        current1 = current1.next
    while current2:
        the_result.append(current2.value)
        current2 = current2.next
    return the_result

if __name__=="__main__":
    ll = LinkedList()
    ll.append(1)
    ll.append(3)
    ll.append(2)
    ll2 = LinkedList()
    ll2.append(5)
    ll2.append(9)
    ll2.append(4)
    print(zip_linked_list(ll,ll2))
