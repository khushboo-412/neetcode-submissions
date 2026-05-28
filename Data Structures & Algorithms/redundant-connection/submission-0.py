class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        adj = [[] for _ in range(n+1)]
        indegree = [0]*(n+1)

        for u,v in edges:
            adj[u].append(v)
            adj[v].append(u)
            indegree[u] += 1
            indegree[v] += 1

        queue =deque()
        for i in range(1, n+1):
            if indegree[i] == 1:
                queue.append(i)

        
        while queue:
            node = queue.popleft()

            for nei in adj[node]:
                indegree[nei] -= 1
                if indegree[nei] == 1:
                    queue.append(nei)



        for u,v in reversed(edges):
            if indegree[u]>1 and indegree[v]>1:
                return [u,v]
        
        return []


            