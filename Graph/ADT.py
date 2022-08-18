class ADTDisjointSet:

    def __init__(self):
        self.parent = {}
        # stores the depth of trees
        self.rank = {}
        self.make_set()

    def make_set(self, elements=None):
        """create `n` disjoint sets (one for each item)"""
        if not elements:
            return

        if isinstance(elements, (list, tuple)):
            elements = [elements]

        for element in elements:
            self.parent[element] = element
            self.rank[element] = 0

    def find(self, k):
        """Find the root of the set in which element `k` belongs
        if `k` is not the root.
        """
        if self.parent[k] != k:
            self.parent[k] = self.find(self.parent[k])
        return self.parent[k]

    def union(self, a, b):
        """Perform Union of two subsets
        find the root of the sets in which elements `x` and `y` belongs.
        """
        x = self.find(a)
        y = self.find(b)

        # if `x` and `y` are present in the same set
        if x == y:
            return

        # Always attach a smaller depth tree under the root of the deeper tree.
        if self.rank[x] > self.rank[y]:
            self.parent[y] = x
        elif self.rank[x] < self.rank[y]:
            self.parent[x] = y
        else:
            self.parent[x] = y
            self.rank[y] += 1


if __name__ == '__main__':
    universe = ['a', 'b', 'c', 'd', 'e', 'h', 'i']
    adt = ADTDisjointSet()
    adt.make_set(universe)
    adt.union('b', 'd')
    adt.union('h', 'b')
    print(adt.find('h'))
    adt.union('h', 'i')
    print(adt.find('i'))
