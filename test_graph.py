from Graph import Graph

def test_graph():

    g = Graph([
        [1, 0, 0],
        [0, 1, 0],
        [0, 0, 1]
    ])

    assert g.vertices() == [
        [1, 0, 0],
        [0, 1, 0],
        [0, 0, 1]
    ]

    assert g.edges() == [
        [1, 1], [2, 2], [3, 3]
    ]

    g = Graph([
        [0, 1, 0, 1],
        [1, 0, 1, 0],
        [0, 1, 0, 1],
        [1, 0, 1, 0]
    ])


    assert g.edges() == [
        [1, 2], [1, 4], [2, 1], [2, 3], [3, 2], [3, 4], [4, 1], [4, 3]
    ]

    pass