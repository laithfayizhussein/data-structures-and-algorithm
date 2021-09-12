from graph_breadth_first import __version__


def test_version():
    assert __version__ == '0.1.0'
import pytest
from graph_breadth_first.graph_breadth import *

def test_happy_path():
    graph2 = Graph()
    hi= graph2.add_node('hi')
    there= graph2.add_node('there')
    greeting= graph2.add_node('greeting')
    come= graph2.add_node('come')
    wlcome= graph2.add_node('wlcome')
    how_are_you= graph2.add_node('how_are_you')
    graph2.add_edge(hi,there)
    graph2.add_edge(there,hi)
    graph2.add_edge(there,greeting)
    graph2.add_edge(there,greeting)
    graph2.add_edge(greeting,there)
    graph2.add_edge(greeting,how_are_you)
    graph2.add_edge(greeting,wlcome)
    graph2.add_edge(greeting,come)
    graph2.add_edge(come,greeting)
    graph2.add_edge(come,wlcome)
    graph2.add_edge(wlcome,come)
    graph2.add_edge(wlcome,greeting)
    graph2.add_edge(wlcome,how_are_you)
    graph2.add_edge(how_are_you,wlcome)
    graph2.add_edge(how_are_you,there)
    graph2.add_edge(how_are_you,greeting)

    actual=graph2.BreadthFirst(hi)
    expected=[hi,there,greeting,how_are_you,wlcome,come]
    assert actual==expected



def test_edge_case():
    graph2 = Graph()
    hi=Top('hi')

    actual=graph2.BreadthFirst(hi)
    expected='This node not in the graph'
    assert actual==expected


def test_expected_failure():
    graph2 = Graph()
    hi= graph2.add_node('hi')
    there= graph2.add_node('there')
    greeting= graph2.add_node('greeting')
    come= graph2.add_node('come')
    wlcome= graph2.add_node('wlcome')
    how_are_you= graph2.add_node('how_are_you')
    graph2.add_edge(hi,there)
    graph2.add_edge(there,hi)
    graph2.add_edge(there,greeting)
    graph2.add_edge(there,greeting)
    graph2.add_edge(greeting,there)
    graph2.add_edge(greeting,how_are_you)
    graph2.add_edge(greeting,wlcome)
    graph2.add_edge(greeting,come)
    graph2.add_edge(come,greeting)
    graph2.add_edge(come,wlcome)
    graph2.add_edge(wlcome,come)
    graph2.add_edge(wlcome,greeting)
    graph2.add_edge(wlcome,how_are_you)
    graph2.add_edge(how_are_you,wlcome)
    graph2.add_edge(how_are_you,there)
    graph2.add_edge(how_are_you,greeting)

    actual=graph2.BreadthFirst(hi)
    expected=[hi,there,greeting,how_are_you,come,wlcome]
    assert actual!=expected
