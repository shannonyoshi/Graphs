import sys
sys.path.insert(1, '../../projects/graph/')

from graph import Graph
from util import Stack, Queue
def earliest_ancestor(ancestors, starting_node):
    graph = Graph()
    added=set()
    for pair in ancestors:
        if pair[0] not in added:
            graph.add_vertex(pair[0])
            added.add(pair[0])
        if pair[1] not in added:
            graph.add_vertex(pair[1])
            added.add(pair[1])
        graph.add_edge(pair[1], pair[0])
    queue = Queue()
    queue.enqueue([starting_node])

    earliest_ancestor = -1
    max_path_length = 1
    while queue.size() > 0: 
        path = queue.dequeue()
        current_ancestor = path[-1]

        if ((len(path)>=max_path_length) and current_ancestor < earliest_ancestor) or (len(path) > max_path_length): 
            earliest_ancestor = current_ancestor
            max_path_length = len(path)

        for next_vert in graph.get_neighbors(current_ancestor):
            new_path = list(path)
            new_path.append(next_vert)
            queue.enqueue(new_path)   
    return earliest_ancestor 
    
    