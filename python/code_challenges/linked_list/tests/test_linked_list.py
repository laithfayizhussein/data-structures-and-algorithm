
from linked_list import __version__
from linked_list.linked_list import LinkedList

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
    linkList.insert_after(2, 1)

    actual = linkList.__str__()
    expected='( 1 ) -> ( 2 ) -> ( 3 ) -> ( 4 ) -> null'
    assert actual==expected

def test_before_middle():
    linkList = LinkedList()
    linkList.append(1)
    linkList.append(3)
    linkList.append(4)
    linkList.insert_before(3, 2)

    actual = linkList.__str__()
    expected='( 1 ) -> ( 2 ) -> ( 3 ) -> ( 4 ) -> null'
    assert actual==expected


def test_after_middle():
    linkList = LinkedList()
    linkList.append(1)
    linkList.append(2)
    linkList.append(4)
    linkList.insert_after(2, 3)

    actual = linkList.__str__()
    expected='( 1 ) -> ( 2 ) -> ( 3 ) -> ( 4 ) -> null'
    assert actual==expected

def test_after_end():
    linkList = LinkedList()
    linkList.append(1)
    linkList.append(2)
    linkList.append(3)
    linkList.insert_after(3, 4)

    actual = linkList.__str__()
    expected='( 1 ) -> ( 2 ) -> ( 3 ) -> ( 4 ) -> null'
    assert actual==expected



