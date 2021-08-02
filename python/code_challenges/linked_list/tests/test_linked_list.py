
from linked_list import __version__
from linked_list.linked_list import LinkedList , Node

def test_version():
    assert __version__ == '0.1.0'

def test_instantiate_empty_linked_list():
    linkList = LinkedList()
    linkList.append()
    actual = linkList.__str__()
    expected='( null ) -> null'
    assert actual==expected

def test_insert():
    linkList = LinkedList()
    linkList.append(5)
    linkList.append(6)
    linkList.insert(4)
    actual=linkList.head.value
    expected=4
    assert actual==expected

def test_head_value():
    linkList = LinkedList()
    linkList.insert(4)
    actual=linkList.head.value
    expected=4
    assert actual==expected

def test_insert_head_value():
    linkList = LinkedList()
    linkList.insert(1)
    linkList.insert('6')
    linkList.insert(5)
    actual = linkList.__str__()
    expected='( 5 ) -> ( 6 ) -> ( 1 ) -> null'
    assert actual==expected

def test_includes_True():
    linkList = LinkedList()
    linkList.append(1)
    linkList.append(2)
    linkList.append(3)
    actual = linkList.includes(1)
    expected=True
    assert actual==expected

def test_includes_False():
    linkList = LinkedList()
    linkList.append(1)
    linkList.append(2)
    linkList.append(3)
    actual = linkList.includes(4)
    expected=False
    assert actual==expected
linkList = LinkedList()

def test_return_linkList_values():
    linkList = LinkedList()
    linkList.append(1)
    linkList.append(2)
    linkList.append(3)
    actual = linkList.__str__()
    expected='( 1 ) -> ( 2 ) -> ( 3 ) -> null'
    assert actual==expected


def test_before_head():
    linkList = LinkedList()
    linkList.append(2)
    linkList.append(3)
    linkList.append(4)
    linkList.insertAfter(2, 1)
    actual = linkList.__str__()
    expected='( 1 ) -> ( 2 ) -> ( 3 ) -> ( 4 ) -> null'
    assert actual==expected

def test_before_middle():
    linkList = LinkedList()
    linkList.append(1)
    linkList.append(3)
    linkList.append(4)
    linkList.insertBefore(3, 2)

    actual = linkList.__str__()
    expected='( 1 ) -> ( 2 ) -> ( 3 ) -> ( 4 ) -> null'
    assert actual==expected


def test_after_middle():
    linkList = LinkedList()
    linkList.append(1)
    linkList.append(2)
    linkList.append(4)
    linkList.insertAfter(2, 3)

    actual = linkList.__str__()
    expected='( 1 ) -> ( 2 ) -> ( 3 ) -> ( 4 ) -> null'
    assert actual==expected

def test_after_end():
    linkList = LinkedList()
    linkList.append(1)
    linkList.append(2)
    linkList.append(3)
    linkList.insertAfter(3, 4)
    actual = linkList.__str__()
    expected='( 1 ) -> ( 2 ) -> ( 3 ) -> ( 4 ) -> null'
    assert actual==expected

# globals for the tests:
link = LinkedList()
link.insert(6)
link.append(9)

# k in the middle some where
def test_nth():
    link.kthFromEnd(3)
    actual = 0
    expected = 0
    assert actual == expected

# k is greater than the length of the linked list
def test_greater_nth():
    link.kthFromEnd(9)
    actual = 'Number is greater than the end of the list'
    expected = 'Number is greater than the end of the list'
    assert actual == expected

# Where k and the length of the list are the same
def test_same_nth():
    link.kthFromEnd(3)
    actual = 5
    expected = 5
    assert actual == expected

# Where k is not a positive integer
def test_negative_nth():
    link.kthFromEnd(-3)
    actual = 'Negative number has been entered'
    expected = 'Negative number has been entered'
    assert actual == expected

# Where the linked list is of a size 1
def test_one_nth():
    new_ll = LinkedList()
    new_ll.insert(1)
    new_ll.kthFromEnd(1)
    actual = 2
    expected = 2
    assert actual == expected
