from PriorityQueue.MinHeap import MinHeap
from ADT import ADTDisjointSet


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
        return '{} adjacent: {}'.format(
            self.id, [(x.id, self.get_weight(x)) for x in self.adjacent])


class Graph:
    def __init__(self, directed=False):
        self.vertices = {}
        self.num_vertices = 0
        self._directed_graph = directed

    def __iter__(self):
        return next(self)

    def __next__(self):
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

    def prims_algorithm_route(self):
        path = ''
        for node in self:
            if node.distance != 0:
                path = '{}Vertex({}) --> Vertex({}), Cost: {}\n'.format(
                    path, node.previous.get_id(), node.get_id(), node.distance)
        return path

    def _prims_algorithm_cost(self):
        cost = 0
        for node in self:
            cost += node.distance
        return cost

    def prims_algorithm(self, start_vertex=None):
        """Time complexity: O(V ^ 2)"""
        # Set the distance for the start node to zero
        if start_vertex is None:
            start = next(iter(self))
        else:
            start = self.get_vertex(start_vertex)
        start.distance = 0
        # Put tuple pair into min heap
        min_heap = MinHeap()
        for item in self:
            min_heap.insert(item)
        min_heap.min_heapify()
        unvisited = min_heap.heap[1:]

        while len(unvisited):
            current_vertex = min_heap.get_min()
            current_vertex.visited = True

            for neighbor in current_vertex.get_connections():
                distance = current_vertex.get_weight(neighbor)
                if neighbor.visited:
                    if neighbor.distance > distance:
                        neighbor.distance = distance
                        neighbor.previous = current_vertex
                    continue

                if distance < neighbor.distance:
                    neighbor.distance = distance
                    neighbor.previous = current_vertex

            # Rebuild heap
            # 1. Pop every item
            min_heap.clear()
            # 2. Put all vertices not visited into the queue
            unvisited = [v for v in self if not v.visited]
            for item in self:
                if not item.visited:
                    min_heap.insert(item)
            min_heap.min_heapify()

        return self._prims_algorithm_cost()

    def kruskal_algorithm(self):
        """Kruskal's algorithm Steps:
            1. Sort all the edges in non-decreasing order of their weight.
            2. Pick the smallest edge. Check if it forms a cycle with the
               spanning tree formed so far. If cycle is not formed,
               include this edge. Else, discard it.
            3. Repeat step#2 until there are (V-1) edges in the spanning tree.

        Time Complexity: O(ELogE + ELogV)
        """
        edges = []
        adt = ADTDisjointSet()
        for vertex in self:
            adt.make_set(vertex.get_id())
            for neighbor in vertex.get_connections():
                weight = vertex.get_weight(neighbor)
                vid = vertex.get_id()
                nid = neighbor.get_id()
                edges.append((weight, vid, nid))

        # Sort edges by their weight
        edges = sorted(edges, key=lambda item: item[0])

        minimum_spanning_tree = set()
        cost = 0
        for edge in edges:
            weight, source_vertex, destination_vertex = edge
            if adt.find(source_vertex) != adt.find(destination_vertex):
                cost += weight
                adt.union(source_vertex, destination_vertex)
                minimum_spanning_tree.add(edge)

        mst = ''
        for _edge in minimum_spanning_tree:
            mst = '{}Source({}) -> Destination({}), Cost: {}\n'.format(
                mst, _edge[1], _edge[2], _edge[0]
            )

        return {
            'cost': cost,
            'minimum_spanning_tree': mst,
        }


if __name__ == '__main__':

    g = Graph()
    g.add_vertex('a')
    g.add_vertex('b')
    g.add_vertex('c')
    g.add_vertex('d')
    g.add_vertex('e')
    g.add_vertex('f')
    g.add_vertex('g')
    g.add_vertex('h')
    g.add_vertex('i')

    g.add_edge('a', 'b', 4)
    g.add_edge('a', 'h', 8)
    g.add_edge('b', 'h', 11)
    g.add_edge('b', 'c', 8)
    g.add_edge('c', 'd', 7)
    g.add_edge('c', 'i', 2)
    g.add_edge('c', 'f', 4)
    g.add_edge('d', 'e', 9)
    g.add_edge('d', 'f', 14)
    g.add_edge('e', 'f', 10)
    g.add_edge('g', 'f', 2)
    g.add_edge('g', 'i', 6)
    g.add_edge('g', 'h', 1)
    g.add_edge('h', 'i', 7)

    result = g.kruskal_algorithm()
    print(result['cost'])
    print(result['minimum_spanning_tree'])
