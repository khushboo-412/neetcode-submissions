class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges)!= (n-1):
            return False
        adj = [[] for _ in range(n)]
        indegree = [0]*n
        for u,v in edges:
            adj[u].append(v)
            adj[v].append(u)
            indegree[u] +=1
            indegree[v] +=1

        queue =deque()
        for i in range(n):
            if indegree[i] <=1:
                queue.append(i)
        
        visited =0

        while queue:
            node = queue.popleft()
            visited  += 1

            for nei in adj[node]:
                indegree[nei] -= 1
                if indegree[nei] == 1:
                    queue.append(nei)
            
        return visited == n



