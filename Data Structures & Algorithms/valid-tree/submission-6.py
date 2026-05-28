class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges)!= (n-1):
            return False
        adj = [[] for _ in range(n)]
        for u,v in edges:
            adj[u].append(v)
            adj[v].append(u)
        

        visited = set()

        def dfs(i,prev):
            if i in visited:
                return False

            visited.add(i)
            for nei in adj[i]:
                if nei == prev:
                    continue

                if dfs(nei,i) == False:
                    return False

        dfs(0,-1) 
        return len(visited) == n