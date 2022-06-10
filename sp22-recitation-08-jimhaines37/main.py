from collections import defaultdict

def make_undirected_graph(edge_list):
    """ Makes an undirected graph from a list of edge tuples. """
    graph = defaultdict(set)
    for e in edge_list:
        graph[e[0]].add(e[1])
        graph[e[1]].add(e[0])
    return graph


def reachable(graph, start_node):
    """
    Returns:
      the set of nodes reachable from start_node
    """

    #Given a graph, iterate through frontier and pop one to add to "visited" set (if it is not already in the "visited" set) (use "pop" so we can remove it from the frontier at the same time)
    #Now a "next" variable can hold a list of neighbors of the popped node using the graph structure
    #Remove nodes already in visited set from the "next" variable so that we have only nodes we have yet to visit
    #New frontier is now the current frontier with the contents of the "next" node added to it
    #Finally return result to get the list of nodes that one can reach from the start node

    result = set([start_node])
    frontier = set([start_node])

    while len(frontier) != 0:
        visitedNode = frontier.pop() 
        
        if visitedNode not in result:
            result.add(visitedNode)

        nextNode = graph[visitedNode]
        nextNode = nextNode.difference(result)
        frontier = frontier.union(nextNode)

    return result

def test_reachable():
    graph = make_undirected_graph([('A', 'B'), ('B', 'C'), ('C', 'D'), ('D', 'B')])
    assert sorted(reachable(graph, 'A')) == ['A', 'B', 'C', 'D']

    graph = make_undirected_graph([('A', 'B'), ('B', 'C'), ('C', 'D'), ('D', 'B'), ('E', 'F'), ('F', 'G')])
    assert sorted(reachable(graph, 'A')) == ['A', 'B', 'C', 'D']
    assert sorted(reachable(graph, 'E')) == ['E', 'F', 'G']




def connected(graph):
    """
    Returns:
      boolean if the graph is connected or not, if one can reach every node from the start node
    """

    #Get number of nodes in graph and store in a variable, get set of reachable nodes from start node using reachable()
    #Compare these 2 values, if they are equal, the graph is connected

    numNodes = len(graph)
    connect = reachable(graph, list(graph.keys())[0])
    return len(connect) == numNodes

def test_connected():
    graph = make_undirected_graph([('A', 'B'), ('B', 'C'), ('C', 'D'), ('D', 'B')])
    assert connected(graph) == True
    graph = make_undirected_graph([('A', 'B'), ('B', 'C'), ('C', 'D'), ('D', 'B'), ('E', 'F'), ('F', 'G')])
    assert connected(graph) == False



def n_components(graph):
    """
    Returns:
      the number of connected components in an undirected graph
    """

    #Create a "frontier" using a list of keys, create result variable to store visited nodes as they leave the frontier
    #Iterate through frontier, pop a node each time and get set of nodes it can reach using reachable(), then remove its set of reachable nodes from frontier 
    #Add reachable values to result variable, and then return the length of this result variable

    result = []
    frontier = set(list(graph.keys()))

    while len(frontier) != 0:
        node = frontier.pop()
        connected = reachable(graph, node)
        frontier = frontier - connected
        result.append(connected)

    return len(result)
    

def test_n_components():
    graph = make_undirected_graph([('A', 'B'), ('B', 'C'), ('C', 'D'), ('D', 'B')])
    assert n_components(graph) == 1

    graph = make_undirected_graph([('A', 'B'), ('B', 'C'), ('C', 'D'), ('D', 'B'), ('E', 'F'), ('F', 'G')])
    assert n_components(graph) == 2



graph = make_undirected_graph([('A', 'B'), ('B', 'C'), ('C', 'D'), ('C', 'E'), ('G','F')])

print("starting graph: ", graph)

print("reachable: ", reachable(graph, 'A'))

print("connected: ", connected(graph))

print("n_components: ", n_components(graph))




