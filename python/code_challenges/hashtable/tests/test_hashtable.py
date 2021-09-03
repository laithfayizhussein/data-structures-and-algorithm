from hashtable import __version__
import pytest

def test_version():
    assert __version__ == '0.1.0'

from hashtable.hash_table import *

def test_add_hashtable(prepared_hashtable):
    prepared_hashtable.add('hello', 30)
    assert prepared_hashtable.get('hello')==30

def test_get_hashtable(prepared_hashtable):
    actual=prepared_hashtable.get('laith')
    expected=88
    assert actual==expected

def test_get_hashtable_incorrect_key(prepared_hashtable):
    actual=prepared_hashtable.get('fayiz')
    expected=None
    assert actual==expected


def test_collision_hashtable(prepared_hashtable):
    actual=prepared_hashtable.contains('laith')
    expected=True
    assert actual==expected

def test_collision_value_hashtable(prepared_hashtable):
    actual=prepared_hashtable.get('liath')
    expected=45
    assert actual==expected


def test_collision_value_hashtable(prepared_hashtable):
    actual=prepared_hashtable.hash('laith')
    expected=854
    assert actual==expected





@pytest.fixture
def prepared_hashtable():
    hashtable = Hashtable(1024)
    hashtable.add('laith', 88)
    hashtable.add('liath', 45)
    hashtable.add('try', True)
    hashtable.add('say', 'Hey')
    hashtable.add('hi', 'world')
    return hashtable
