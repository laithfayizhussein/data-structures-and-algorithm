from hashmap_left_join import __version__


def test_version():
    assert __version__ == '0.1.0'


from hashmap_left_join.hashmap_left_join import *
import pytest

def test_happy_path(prepared_hash1,prepared_hash2):

    actual=left_join(prepared_hash1,prepared_hash2)
    expected=[['wrath', 'anger', 'delight'], ['outfit','grap', None], ['diligent','employed','idle'], ['guide','usher','follow'], ['fond', 'enamored','averse']]
    assert actual==expected

def test_edge_case():
    ht1 =Hash_table()
    ht2 =Hash_table()
    actual=left_join(ht1,ht2)
    expected='hash table is empty'
    assert actual==expected

def test_expected_failure(prepared_hash1):
    ht2 =Hash_table()
    ht2.add('hi','averse')
    ht2.add('wrath','delight')
    ht2.add('diligent','idle')
    ht2.add('guide','follow')
    ht2.add('flow','jam')
    actual=left_join(prepared_hash1,ht2)
    expected=[['wrath', 'anger','delight'], ['outfit', 'grap', None], ['diligent','employed','idle'], ['guide','usher','follow'], ['fond', 'enamored','averse']]
    assert actual!=expected

@pytest.fixture
def prepared_hash1():
    ht1 = Hash_table()
    ht1.add('fond','enamored')
    ht1.add('wrath','anger')
    ht1.add('diligent','employed')
    ht1.add('outfit','grap')
    ht1.add('guide','usher')
    return ht1

@pytest.fixture
def prepared_hash2():
    ht2 = Hash_table()
    ht2.add('fond','averse')
    ht2.add('wrath','delight')
    ht2.add('diligent','idle')
    ht2.add('guide','follow')
    ht2.add('flow','jam')
    return ht2
