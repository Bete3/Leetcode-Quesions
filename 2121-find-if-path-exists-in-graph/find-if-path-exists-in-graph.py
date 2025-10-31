class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        graph = {i: [] for i in range(n)}
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        def traverse(graph,source):
            
            visited = set()
            stack = [source]
            result = []
            while stack:
                node = stack.pop()
                if node not in visited:
                    visited.add(node)
                    result.append(node)
                    stack.extend(reversed(graph[node]))
            if destination in result:
                return True
            else:
                return False
        return traverse(graph,source)
        
          