class WeightedGraph:

    def __init__(self):
        self._edges = None
        self.graph = {}

    def add_edges(self, edges):
        for _edge in edges:
            self._add_edge(*_edge)

    def add_edge(self, *args, **kwargs):
        self._add_edge(*args, **kwargs)

    def _add_edge(self, source, destination, weight=None):
        _edge = {'target': destination, 'weight': weight}
        if source in self.graph:
            self.graph[source].append(_edge)
        else:
            self.graph[source] = [_edge]

    def get_paths(self, source, destination, path=None):
        if path is None:
            path = []
        path = path + [source]

        if source == destination:
            return [path]

        if source not in self.graph:
            return []

        paths = []
        for node in self.graph[source]:
            if node['target'] not in path:
                new_paths = self.get_paths(
                    node['target'], destination, path=path)
                for _path in new_paths:
                    paths.append(_path)
        return paths

    def get_shortest_path(self, source, destination, path=None):
        if path is None:
            path = []
        path = path + [source]
        if source == destination:
            return path

        if source not in self.graph:
            return None

        shortest_path = None
        for node in self.graph[source]:
            if node['destination'] not in path:
                _shortest_path = self.get_shortest_path(
                    node['destination'], destination, path=path)
                if _shortest_path:
                    if shortest_path is None or len(_shortest_path) < len(shortest_path):
                        shortest_path = _shortest_path

        return shortest_path


if __name__ == '__main__':
    routes = [
        ('Mumbai', 'Paris', 10),
        ('Mumbai', 'Dubai', 20),
        ('Paris', 'Dubai', 30),
        ('Paris', 'New York', 10),
        ('Dubai', 'New York', 50),
        ('New York', 'Toronto', 5),
    ]

    route_graph = WeightedGraph()
    route_graph.add_edges(routes)

    print(route_graph.get_paths('Mumbai', 'New York'))
    print(route_graph.graph)
    print(route_graph.get_shortest_path('Paris', 'New York'))
