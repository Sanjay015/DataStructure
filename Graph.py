class Graph:

    def __init__(self, edges):
        self.edges = edges
        self.graph_dict = {}
        for source, destination in self.edges:
            if source in self.graph_dict:
                self.graph_dict[source].append(destination)
            else:
                self.graph_dict[source] = [destination]

    def get_paths(self, source, destination, path=None):
        if path is None:
            path = []
        path = path + [source]

        if source == destination:
            return [path]

        if source not in self.graph_dict:
            return []

        paths = []
        for node in self.graph_dict[source]:
            if node not in path:
                new_paths = self.get_paths(node, destination, path)
                for _path in new_paths:
                    paths.append(_path)
        return paths

    def get_shortest_path(self, source, destination, path=None):
        if path is None:
            path = []
        path = path + [source]
        if source == destination:
            return path

        if source not in self.graph_dict:
            return None

        shortest_path = None
        for node in self.graph_dict[source]:
            if node not in path:
                _shortest_path = self.get_shortest_path(node, destination, path)
                if _shortest_path:
                    if shortest_path is None or len(_shortest_path) < len(shortest_path):
                        shortest_path = _shortest_path

        return shortest_path


if __name__ == '__main__':
    routes = [
        ('Mumbai', 'Paris'),
        ('Mumbai', 'Dubai'),
        ('Paris', 'Dubai'),
        ('Paris', 'New York'),
        ('Dubai', 'New York'),
        ('New York', 'Toronto'),
    ]

    route_graph = Graph(routes)

    # print(route_graph.get_paths('Mumbai', 'Mumbai'))
    # print(route_graph.get_paths('Toronto', 'New York'))
    # print(route_graph.get_paths('Mumbai', 'New York'))
    print(route_graph.get_shortest_path('Mumbai', 'New York'))
    print(route_graph.get_shortest_path('Paris', 'New York'))
