from hashmap_tree_intersection import __version__

def test_version():
    assert __version__ == '0.1.0'

import pytest
from hashmap_tree_intersection.hashmap_tree_intersection import *

def test_happy_path(prepared_f_tree,prepared_s_tree):
    actual=intersection(prepared_f_tree,prepared_s_tree)
    expected=[100, 160, 125, 175, 200, 350, 500]
    assert actual==expected


def test_edge_case():
    f_tree=BinaryTree()
    s_tree=BinaryTree()
    actual=intersection(f_tree,s_tree)
    expected='theres emptry tree'
    assert actual==expected


def test_expected_failure(prepared_f_tree,prepared_s_tree):
    prepared_f_tree.root.left=Node2(600)
    actual=intersection(prepared_f_tree,prepared_s_tree)
    expected=[100, 160, 125, 175, 200, 350, 500]
    assert actual!=expected


@pytest.fixture
def prepared_f_tree():
    f_tree=BinaryTree()
    f_tree.root=Node2(150)
    f_tree.root.left=Node2(100)
    f_tree.root.right=Node2(250)
    f_tree.root.left.left=Node2(75)
    f_tree.root.left.right=Node2(160)
    f_tree.root.right.left=Node2(200)
    f_tree.root.right.right=Node2(350)
    f_tree.root.left.right.left=Node2(125)
    f_tree.root.left.right.right=Node2(175)
    f_tree.root.right.right.left=Node2(300)
    f_tree.root.right.right.right=Node2(500)
    return f_tree

@pytest.fixture
def prepared_s_tree():
    s_tree=BinaryTree()
    s_tree.root=Node2(42)
    s_tree.root.left=Node2(100)
    s_tree.root.right=Node2(600)
    s_tree.root.left.left=Node2(15)
    s_tree.root.left.right=Node2(160)
    s_tree.root.right.left=Node2(200)
    s_tree.root.right.right=Node2(350)
    s_tree.root.left.right.left=Node2(125)
    s_tree.root.left.right.right=Node2(175)
    s_tree.root.right.right.left=Node2(4)
    s_tree.root.right.right.right=Node2(500)
    return s_tree
