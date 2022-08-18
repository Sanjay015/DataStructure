from DSQueue import DSQueue
from Stack.Stack import Stack
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
        return '{} adjacent: {}'.format(self.id, [x.id for x in self.adjacent])


class Graph:
    def __init__(self):
        self.vertices = {}
        self.num_vertices = 0

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
        self.vertices[destination].add_neighbor(self.vertices[source], weight)

    def get_vertices(self):
        for vertex in self.vertices.keys():
            yield vertex

    def get_edges(self):
        edges = []
        for vertex in self:
            for connection in vertex.get_connections():
                edges.append((vertex.get_id(), connection.get_id()))
        return edges

    def _dfs(self, current_vertex, visited):
        visited[current_vertex] = True
        for neighbour in current_vertex.get_connections():
            if neighbour not in visited:
                self._dfs(neighbour, visited)

    def dfs_traversal(self):
        visited = {}
        for current_vertex in self:
            self._dfs(current_vertex, visited)

    def _bfs(self, vertex_id):
        start = self.get_vertex(vertex_id)
        start.distance = 0
        start.previous = None
        queue = DSQueue.Queue()
        queue.enqueue(start)

        while not queue.is_empty():
            vertex = queue.dequeue()
            for neighbour in vertex.data.get_connections():
                if not neighbour.visited:
                    neighbour.distance = vertex.data.distance + 1
                    neighbour.previous = vertex.data
                    queue.enqueue(neighbour)
                vertex.data.visited = True

    def bfs_traversal(self):
        for vertex in self:
            if not vertex.visited:
                self._bfs(vertex.get_id())

    def _get_shortest_path(self, vertex, result=None):
        """make shortest path from v.previous"""
        if result is None:
            result = Stack()
        if vertex.previous:
            result.push(vertex.previous.get_id())
            self._get_shortest_path(vertex.previous, result=result)
        return result

    def dijkstra_algorithm(self, start_vertex, end_vertex):
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
                weight = current_vertex.get_weight(neighbor)
                distance = current_vertex.distance + weight

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

        end_vertex = self.get_vertex(end_vertex)
        _result = Stack()
        _result.push(end_vertex.get_id())
        _shortest_path = self._get_shortest_path(end_vertex, result=_result)
        return {
            'shortest_path': str(_shortest_path),
            'weight': end_vertex.distance,
        }

    def bellman_ford_algorithm(self, source):
        """Dijkstra algorithm does not work with negative edge cost.
        Assume cost to vertex V is very highly negative from some other vertex
        V1, in this case path from V2 to V1 is back to V is better that going
        from V2 to V is without using V1. A combination of Dijkstra and
        unweighted algorithm will solve the problem. Find all vertices as:
            distance to V1 + weight(v, w) < old distance to w
        """
        distance = {}

        for vertex in self:
            # Assuming all the nodes are very far
            distance[vertex.get_id()] = float('inf')

        distance[source] = 0

        for vertex in self:
            for neighbor in vertex.get_connections():
                vertex_weight = distance[vertex.get_id()]
                w = vertex.get_weight(neighbor)
                nw = distance[neighbor.get_id()]
                if vertex_weight != float('inf') and vertex_weight + w < nw:
                    distance[neighbor.get_id()] = vertex_weight + w

        for v in self:
            for n in v.get_connections():
                try:
                    assert distance[v.get_id()] <= distance[n.get_id()] + v.get_weight(n)
                except Exception:
                    print(v.get_id(), n.get_id(), distance[v.get_id()], distance[n.get_id()], v.get_weight(n))
        print('------', distance)


if __name__ == '__main__':
    g = Graph()
    g.add_vertex('a')
    g.add_vertex('b')
    g.add_vertex('c')
    g.add_vertex('d')
    g.add_vertex('e')

    # g.add_edge('a', 'b', 4)
    # g.add_edge('a', 'c', 1)
    # g.add_edge('c', 'b', 2)
    # g.add_edge('b', 'e', 4)
    # g.add_edge('c', 'd', 4)
    # g.add_edge('d', 'e', 4)
    # g.dfs_traversal()
    # g.bfs_traversal()

    # print(g.dijkstra_algorithm('a', 'e'))
    g.add_edge('a', 'b', 2)
    g.add_edge('a', 'c', 1)
    g.add_edge('c', 'b', 5)
    g.add_edge('b', 'e', 5)
    g.add_edge('c', 'd', 4)
    g.add_edge('d', 'e', -1)

    print(g.bellman_ford_algorithm('a'))
