from algo_crate.datastructures.priority_queue import PriorityQueue


def dijkstra(G, s):
    G.reset(initial_vertex_properties={
        "pred": None,
        "d": float("inf"),
    })
    s.properties["d"] = 0

    S = set()
    Q = PriorityQueue(G.vertices, key=lambda x: x.properties["d"])

    while not Q.is_empty():
        u = Q.dequeue()
        S.add(u)

        for e in u.edges:
            v, w = e.v, e.w
            dist_v = u.properties["d"] + w
            if dist_v < v.properties["d"]:
                v.properties["d"] = dist_v
                v.properties["pred"] = u

            if v in Q:
                Q.decrease_key(v)
            else:
                Q.enqueue(v)

