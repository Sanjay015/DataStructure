from PriorityQueue.MinHeap import MinHeap


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

    def prims_algorithm(self, start_vertex):
        # Set the distance for the start node to zero
        start = self.get_vertex(start_vertex)
        start.distance = 0

        # Put tuple pair into min heap
        min_heap = MinHeap()
        for item in self:
            min_heap.insert(item)
        min_heap.min_heapify()
        unvisited = min_heap.heap[1:]

        # while not queue.is_empty():
        while len(unvisited):
            current_vertex = min_heap.get_min()
            current_vertex.visited = True

            for neighbor in current_vertex.get_connections():
                # if visited do not bother
                if neighbor.visited:
                    continue
                distance = current_vertex.get_weight(neighbor)

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

    def kruskal_algorithm(self, start_vertex):
        edges = []
        for vertex in self:
            pass


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

    g.prims_algorithm('a')
    for v, val in g.vertices.items():
        print(v, val)
