from graph import Graph
from util import Queue


def earliest_ancestor(ancestors, starting_node):
    # Create a graph
    g = Graph()
    # Loop through ancestors and add vertices to graph
    for ancestor in ancestors:
        parent, child = ancestor
        if parent not in g.vertices:
            g.add_vertex(parent)
        if child not in g.vertices:
            g.add_vertex(child)
        g.add_edge(child, parent)

    # Create a queue for graph traversal
    q = Queue()
    # Add starting node
    q.enqueue([starting_node])
    # Create a set to store visited vertices
    visited = set()
    earliest = -1
    while q.size() > 0:
        path = q.dequeue()
        vertex = path[-1]
        if vertex not in visited:
            visited.add(vertex)
            if (vertex < earliest) or (len(path) > 1):
                earliest = vertex
        for neighbor in g.vertices[vertex]:
                new_path = list(path)
                new_path.append(neighbor)
                q.enqueue(new_path)
    return earliest


