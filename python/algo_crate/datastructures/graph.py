from copy import deepcopy


class Vertex:

    def __init__(self, id):
        self.id = id
        self.edge_set = {}

        self.properties = {}

    @property
    def edges(self):
        return set(self.edge_set.values())

    @property
    def neighbours(self):
        return map(lambda x: x.v, self.edges)

    def add_edge(self, e):
        self.edge_set[e.v.id] = e

    def remove_edge(self, v):
        del self.edge_set[v.id]

    def reset(self, initial_vertex_properties={}, initial_edge_properties={}):
        self.properties = deepcopy(initial_vertex_properties)
        for e in self.edges:
            e.reset(initial_edge_properties)

    def __eq__(self, other):
        return isinstance(other, Vertex) and self.id == other.id

    def __hash__(self):
        return hash(self.id)

class Edge:

    def __init__(self, u, v, w):
        self.u = u
        self.v = v

        self.w = w

        self.properties = {}

    def reset(self, initial_properties={}):
        self.properties = deepcopy(initial_properties)

    def __eq__(self, other):
        return isinstance(other, Edge) \
               and self.u == other.u and self.v == other.v


class Graph:

    def __init__(self):
        self.vertex_set = {}

    @property
    def vertices(self):
        return self.vertex_set.values()

    def reset(self, initial_vertex_properties={}, initial_edge_properties={}):
        for v in self.vertices:
            v.reset(initial_vertex_properties, initial_edge_properties)

    def add_vertex(self, v):

        if not isinstance(v, Vertex):
            self.add_vertex(Vertex(v))

        self.vertex_set[v.id] = v

    def remove_vertex(self, v):
        assert self.has_vertex(v)

        if not isinstance(v, Vertex):
            self.remove_vertex(self.vertex_set[v])

        del self.vertex_set[v.id]

    def has_vertex(self, v):

        if not isinstance(v, Vertex):
            return v in self.vertex_set

        return self.has_vertex(v.id)

    def add_edge(self, u, v):

        assert self.has_vertex(u) and self.has_vertex(v)
        if not (isinstance(u, Vertex) and isinstance(u, Vertex)):
            self.add_edge(self.vertex_set[u], self.vertex_set[v])

        e1, e2 = Edge(u, v), Edge(v, u)
        u.add_edge(e1)
        v.add_edge(e2)

    def remove_edge(self, u, v):
        assert self.has_vertex(u) and self.has_vertex(v)
        if not (isinstance(u, Vertex) and isinstance(u, Vertex)):
            self.remove_edge(self.vertex_set[u], self.vertex_set[v])

        u.remove_edge(v)
        v.add_edge(u)

