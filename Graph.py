
class Graph:

    def __init__(self, vertices):
        self.v = vertices

        self.e = []

        for i, row in enumerate(vertices):
             for j, adj in enumerate(row):
                if adj == 1:
                    self.e.append([i + 1, j + 1])

        pass

    def vertices(self):
        return self.v
        pass

    pass

    def edges(self):

        return self.e

        pass
