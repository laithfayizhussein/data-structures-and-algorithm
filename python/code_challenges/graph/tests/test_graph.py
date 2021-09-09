from graph import __version__

def test_version():
    assert __version__ == '0.1.0'
from graph.graph import *

import pytest

def test_add():
    graph=Graph()
    actual=graph.add_node('a')
    expected=graph.get_nodes()[0]
    assert actual==expected

def test_edge():
    graph =Graph()
    a=graph.add_node('a')
    b=graph.add_node('b')
    graph.add_edge(a, b)
    actual=graph.get_neighbors(a)[0][0]
    expected=b
    assert actual==expected

def test_get_nodes():
    graph =Graph()
    a =graph.add_node('a')
    b =graph.add_node('b')
    c =graph.add_node('c')
    d =graph.add_node('d')
    e =graph.add_node('e')
    f =graph.add_node('f')
    actual=graph.get_nodes()
    expected=[a,b,c,d,e,f]
    assert actual==expected

def test_get_neighbors_node():
    graph =Graph()
    a = graph.add_node('a')
    c = graph.add_node('c')
    graph.add_edge(a, c)
    actual=graph.get_neighbors(a)[0][0]
    expected=c
    assert actual==expected

def test_get_neighbors_weight():
    graph =Graph()
    a =graph.add_node('a')
    c =graph.add_node('c')
    graph.add_edge(a, c)
    actual=graph.get_neighbors(a)[0][1]
    expected=0
    assert actual==expected

def test_only_one_node():
    graph=Graph()
    a=graph.add_node('a')
    actual=graph.get_neighbors(a)
    expected=[]
    assert actual==expected

def test_empty_graph():
    graph=Graph()
    actual=graph.get_nodes()
    expected=None
    assert actual==expected

@pytest.fixture
def prepared_graph():
    graph = Graph()
    a=graph.add_node('a')
    b=graph.add_node('b')
    c=graph.add_node('c')
    d=graph.add_node('d')
    e=graph.add_node('e')
    f=graph.add_node('f')
    graph.add_edge(a,c)
    graph.add_edge(a,d)
    graph.add_edge(b,c)
    graph.add_edge(b,f)
    graph.add_edge(c,a)
    graph.add_edge(c,b)
    graph.add_edge(c,e)
    graph.add_edge(d,a)
    graph.add_edge(d,e)
    graph.add_edge(e,c)
    graph.add_edge(e,d)
    graph.add_edge(e,f)
    graph.add_edge(f,b)
    graph.add_edge(f,e)
    return graph
