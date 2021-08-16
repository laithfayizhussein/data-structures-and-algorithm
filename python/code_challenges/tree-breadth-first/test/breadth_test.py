from breadth.breadth import (Node, BinaryTree,breadth_first)
import pytest



def test_happy_path(tree):
    assert breadth_first(tree)==[4,8,2,25,9,6,3]
