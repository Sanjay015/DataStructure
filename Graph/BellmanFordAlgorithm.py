class Vertex:
    def __init__(self, node):
        self.id = node
        self.adjacent = {}
        # Set distance to infinity for all nodes
        self._distance = float('inf')
        # Mark all nodes unvisited
        self._visited = False
        # Predecessor
        self._previous = None

    def __lt__(self, other):
        return self.distance < other.distance

    def __le__(self, other):
        return self.distance <= other.distance

    def __gt__(self, other):
        return self.distance > other.distance

    def __ge__(self, other):
        return self.distance >= other.distance

    def __eq__(self, other):
        return self.distance == other.distance

    def __hash__(self):
        return hash('{}'.format(self.id))

    def add_neighbor(self, neighbor, weight=0):
        self.adjacent[neighbor] = weight

    def get_connections(self):
        return self.adjacent.keys()

    def get_id(self):
        return self.id

    def get_weight(self, neighbor):
        return self.adjacent[neighbor]

    @property
    def distance(self):
        return self._distance

    @distance.setter
    def distance(self, dist):
        self._distance = dist

    @property
    def previous(self):
        return self._previous

    @previous.setter
    def previous(self, prev):
        self._previous = prev

    @property
    def visited(self):
        return self._visited

    @visited.setter
    def visited(self, value):
        self._visited = value

    def __str__(self):
        return '{} adjacent: {}'.format(self.id, [x.id for x in self.adjacent])


class Graph:
    def __init__(self, directed=False):
        self.vertices = {}
        self.num_vertices = 0
        self._directed_graph = directed

    def __iter__(self):
        for item in self.vertices.values():
            yield item

    def add_vertex(self, node):
        self.num_vertices += 1
        new_vertex = Vertex(node)
        self.vertices[node] = new_vertex
        return new_vertex

    def get_vertex(self, n):
        return self.vertices.get(n)

    def add_edge(self, source, destination, weight=0):
        if source not in self.vertices:
            self.add_vertex(source)

        if destination not in self.vertices:
            self.add_vertex(destination)
        self.vertices[source].add_neighbor(self.vertices[destination], weight)
        if not self._directed_graph:
            self.vertices[destination].add_neighbor(
                self.vertices[source], weight)

    def get_vertices(self):
        for vertex in self.vertices.keys():
            yield vertex

    def get_edges(self):
        edges = []
        for vertex in self:
            for connection in vertex.get_connections():
                edges.append((vertex.get_id(), connection.get_id()))
        return edges

    def bellman_ford_algorithm(self, source):
        """Dijkstra algorithm does not work with negative edge cost.
        Assume cost to vertex V is very highly negative from some other vertex
        V1, in this case path from V2 to V1 is back to V is better that going
        from V2 to V is without using V1. A combination of Dijkstra and
        unweighted algorithm will solve the problem. Find all vertices as:
            distance to V1 + weight(v, w) < old distance to w

        Bellman-Ford algorithm does not work with undirected graph.
        The standard Bellman-Ford algorithm reports the shortest path only if
        there are no negative weight cycles

        time complexity: O(V * E)
        """
        # In our case we already have vertex with default distance as `inf`
        # No need to run a loop to set all vertices distance to `inf`
        # Set source vertex distance to 0
        source_vertex = self.get_vertex(source)
        source_vertex.distance = 0

        for vertex in self:
            for neighbor in vertex.get_connections():
                _weight_from_source = vertex.distance
                _neighbor_edge_cost = vertex.get_weight(neighbor)
                _neighbor_from_source = neighbor.distance
                _total_cost = _weight_from_source + _neighbor_edge_cost
                if (_weight_from_source != float('inf') and
                        _total_cost < _neighbor_from_source):
                    neighbor.distance = _total_cost

        error_msg = 'Graph contains negative weight cycle'
        for v in self:
            for n in v.get_connections():
                _weight_from_source = v.distance
                _neighbor_edge_cost = v.get_weight(n)
                _neighbor_from_source = n.distance
                _total_cost = _weight_from_source + _neighbor_edge_cost
                assert (_weight_from_source != float('inf') and
                        _neighbor_from_source <= _total_cost), error_msg

        distance = {}
        for _v in self:
            distance[_v.get_id()] = _v.distance
        return distance


if __name__ == '__main__':

    g = Graph(directed=True)
    g.add_vertex('a')
    g.add_vertex('b')
    g.add_vertex('c')
    g.add_vertex('d')
    g.add_vertex('e')

    g.add_edge('a', 'b', -1)
    g.add_edge('a', 'c', 4)
    g.add_edge('b', 'c', 3)
    g.add_edge('b', 'd', 2)
    g.add_edge('b', 'e', 2)
    g.add_edge('d', 'c', 5)
    g.add_edge('d', 'b', 1)
    g.add_edge('e', 'd', -3)

    print(g.bellman_ford_algorithm('a'))
