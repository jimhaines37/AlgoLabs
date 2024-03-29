from collections import deque
from heapq import heappush, heappop 

def shortest_shortest_path(graph, source):
    """
    Params: 
      graph.....a graph represented as a dict where each key is a vertex
                and the value is a set of (vertex, weight) tuples (as in the test case)
      source....the source node
      
    Returns:
      a dict where each key is a vertex and the value is a tuple of
      (shortest path weight, shortest path number of edges). See test case for example.
    """
    def shortest_helper(result, frontier, graph):
      frontlen = len(frontier)

      if frontlen > 0:
          node = heappop(frontier)
          distance = node[0]
          edge = node[1]
          letter = node[2]
          
          if letter not in result:
              result[letter] = (distance, edge)

              for neighbor, weight in graph[letter]:
                heappush(frontier, ((distance + weight), edge + 1, neighbor)) 

          return shortest_helper(result, frontier, graph)
  
      else:
          return result

    result = dict()
    frontier = []
    sourceNode = (0,0, source)
    heappush(frontier, sourceNode)

    return shortest_helper(result, frontier, graph)
    
def test_shortest_shortest_path():

    graph = {
                's': {('a', 1), ('c', 4)},
                'a': {('b', 2)}, # 'a': {'b'},
                'b': {('c', 1), ('d', 4)}, 
                'c': {('d', 3)},
                'd': {},
                'e': {('d', 0)}
            }
    result = shortest_shortest_path(graph, 's')
    # result has both the weight and number of edges in the shortest shortest path
    assert result['s'] == (0,0)
    assert result['a'] == (1,1)
    assert result['b'] == (3,2)
    assert result['c'] == (4,1)
    assert result['d'] == (7,2)
    
    
def bfs_path(graph, source):
    """
    Returns:
      a dict where each key is a vertex and the value is the parent of 
      that vertex in the shortest path tree.
    """
    result = dict() 
    frontier = set([source])

    while len(frontier) > 0:
        newNode = frontier.pop()
        
        for node in graph[newNode]: 
          if node[0] not in result.keys():
            result[node[0]] = newNode
            frontier.add(node[0])

    return result

def get_sample_graph():
     return {'s': {'a', 'b'},
            'a': {'b'},
            'b': {'c'},
            'c': {'a', 'd'},
            'd': {}
            }

def test_bfs_path():
    graph = get_sample_graph()
    parents = bfs_path(graph, 's')
    assert parents['a'] == 's'
    assert parents['b'] == 's'    
    assert parents['c'] == 'b'
    assert parents['d'] == 'c'
    
def get_path(parents, destination):
    """
    Returns:
      The shortest path from the source node to this destination node 
      (excluding the destination node itself). See test_get_path for an example.
    """
    if destination in parents:
        return get_path(parents, parents[destination]) + parents[destination]
    else:
        return ''

def test_get_path():
    graph = get_sample_graph()
    parents = bfs_path(graph, 's')
    assert get_path(parents, 'd') == 'sbc'


graph = {
          's': {('a', 1), ('c', 4)},
          'a': {('b', 2)}, 
          'b': {('c', 1), ('d', 4)}, 
          'c': {('d', 3)},
          'd': {},
          'e': {('d', 0)}
        }

graph2 = {  's': {'a', 'b'},
            'a': {'b'},
            'b': {'c'},
            'c': {'a', 'd'},
            'd': {}
          }

print("function1: ", shortest_shortest_path(graph, 's'))
print("function 2: ", bfs_path(graph, 's'))
parents = bfs_path(graph2, 's')
print("function 3: ", get_path(parents, 'd'))
