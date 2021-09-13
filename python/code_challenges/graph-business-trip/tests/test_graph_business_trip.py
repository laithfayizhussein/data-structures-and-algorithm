from graph_business_trip import __version__


def test_version():
    assert __version__ == '0.1.0'


from graph_business_trip.graph_businsee_trip import *

def test_happy_path():
    g2 = Graph()
    pandora= g2.add_node('pandora')
    arendelle= g2.add_node('arendelle')
    metroville= g2.add_node('metroville')
    narina= g2.add_node('narina')
    naboo= g2.add_node('naboo')
    manstropolis= g2.add_node('manstropolis')

    g2.add_edge(pandora,arendelle,150)
    g2.add_edge(pandora,metroville,82)
    g2.add_edge(arendelle,pandora,150)
    g2.add_edge(arendelle,metroville,99)
    g2.add_edge(arendelle,manstropolis,42)
    g2.add_edge(metroville,pandora,82)
    g2.add_edge(metroville,arendelle,99)
    g2.add_edge(metroville,manstropolis,105)
    g2.add_edge(metroville,naboo,26)
    g2.add_edge(metroville,narina,37)
    g2.add_edge(narina,metroville,37)
    g2.add_edge(narina,naboo,250)
    g2.add_edge(naboo,narina,250)
    g2.add_edge(naboo,metroville,26)
    g2.add_edge(naboo,manstropolis,73)
    g2.add_edge(manstropolis,naboo,73)
    g2.add_edge(manstropolis,arendelle,42)
    g2.add_edge(manstropolis,metroville,105)
    actual=business_trip(g2,[metroville,pandora])
    expected=(True, '$82')
    assert actual==expected

def test_edge_case():
    g2 = Graph()

    pandora= g2.add_node('pandora')
    arendelle= g2.add_node('arendelle')
    metroville= g2.add_node('metroville')
    narina= g2.add_node('narina')
    naboo= g2.add_node('naboo')
    manstropolis= g2.add_node('manstropolis')

    g2.add_edge(pandora,arendelle,160)
    g2.add_edge(pandora,metroville,38)
    g2.add_edge(arendelle,pandora,150)
    g2.add_edge(arendelle,metroville,99)
    g2.add_edge(arendelle,manstropolis,42)
    g2.add_edge(metroville,pandora,100)
    g2.add_edge(metroville,arendelle,80)
    g2.add_edge(metroville,manstropolis,69)
    g2.add_edge(metroville,naboo,95)
    g2.add_edge(metroville,narina,26)
    g2.add_edge(narina,metroville,26)
    g2.add_edge(narina,naboo,800)
    g2.add_edge(naboo,narina,800)
    g2.add_edge(naboo,metroville,26)
    g2.add_edge(naboo,manstropolis,78)
    g2.add_edge(manstropolis,naboo,78)
    g2.add_edge(manstropolis,arendelle,55)
    g2.add_edge(manstropolis,metroville,200)

    actual=business_trip(g2,[arendelle,manstropolis, naboo])
    expected=(False,'$0')
    assert actual==expected


def test_expected_failure():
    g2=Graph()
    pandora=g2.add_node('pandora')
    arendelle=g2.add_node('arendelle')
    metroville=g2.add_node('metroville')
    narina=g2.add_node('narina')
    naboo=g2.add_node('naboo')
    manstropolis=g2.add_node('manstropolis')

    g2.add_edge(pandora,arendelle,44)
    g2.add_edge(pandora,metroville,44)
    g2.add_edge(arendelle,pandora,44)
    g2.add_edge(arendelle,metroville,99)
    g2.add_edge(arendelle,manstropolis,44)
    g2.add_edge(metroville,pandora,44)
    g2.add_edge(metroville,arendelle,44)
    g2.add_edge(metroville,manstropolis,44)
    g2.add_edge(metroville,naboo,44)
    g2.add_edge(metroville,narina,44)
    g2.add_edge(narina,metroville,44)
    g2.add_edge(narina,naboo,44)
    g2.add_edge(naboo,narina,44)
    g2.add_edge(naboo,metroville,44)
    g2.add_edge(naboo,manstropolis,44)
    g2.add_edge(manstropolis,naboo,44)
    g2.add_edge(manstropolis,arendelle,44)
    g2.add_edge(manstropolis,metroville,44)

    actual=business_trip(g2,[arendelle,manstropolis,naboo])
    expected=(True, '$82')
    assert actual!=expected
