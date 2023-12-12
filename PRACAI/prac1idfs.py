from collections import defaultdict

class Graph:
    def __init__(self) -> None:
        self.graph = defaultdict(list)

    def add_edge( self , u  ,v):
        self.graph[u].append(v)
        self.graph[v].append(u)

    def idfs(self , start , end):
        if start == end:
            return [start]
        
        visited = set()
        stack =  [(start , [start])]

        while stack:
            cv , path = stack.pop()
            visited.add(cv)

            for n in  self.graph[cv]:
                if n not in visited:
                    if n == end :
                        return path + [n]
                    stack.append((n , path + [ n]))

        return None
if __name__ == "__main__":
   g = Graph()
   g.add_edge(1,2)
   g.add_edge(1,3)
   g.add_edge(2,4)
   g.add_edge(2,5)
   g.add_edge(3,6)
   g.add_edge(3,7)
   g.add_edge(4,8)
   g.add_edge(4,9)
   g.add_edge(5,10)
   g.add_edge(5,11)
   g.add_edge(6,12)
   g.add_edge(6,13)
   g.add_edge(7,14)
   g.add_edge(7,15)

   start_node = 1
   end_node = 9
   shortest_path = g.idfs(start_node, end_node)

   if shortest_path:
      print(f"Shortest path from {start_node} to {end_node}: {shortest_path}")
   else:
      print(f"No path found from {start_node} to {end_node}.")


"""OUTPUT:-
   Shortest path from 1 to 9: [1, 2, 4, 9]
"""
     