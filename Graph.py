
class Graph:

    def __init__(self, adjacency_matrix):

        self.e = []
        self.v = []

        for i, row in enumerate(adjacency_matrix):
             for j, adj in enumerate(row):
                if adj == 1:
                    self.e.append([i + 1, j + 1])

        for edge in self.e:
            for i in edge:
                if i not in self.v:
                    self.v.append(i)

        self.v.sort()

        pass

    def vertices(self):
        return self.v
        pass

    pass

    def edges(self):

        return self.e

        pass
