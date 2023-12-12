from collections import deque

def bfs(graph  , start):
    visited  = set()
    queue= deque([start])
    while queue :
        vertex = queue.popleft()
        if vertex not in visited:
            visited.add(vertex)
            print(vertex)
            
            #negihbours
            nrighbour = graph[vertex]
            for n in nrighbour:
                if n not in visited:
                    queue.append(n)
graph = {
    'A': ['B' , 'C'] ,
    'B' : ['A' , 'D' , 'E'],
    'C' : [ 'A' , 'F'],
    'D' : [ 'B' ],
    'E' : [ 'B'] ,
    'F' : ['C']
}
start_vertex = 'A'
bfs(graph , start_vertex)        