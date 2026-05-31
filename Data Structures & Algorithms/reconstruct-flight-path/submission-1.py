class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        adj = defaultdict(list)
        tickets.sort()

        for src,des in tickets:
            adj[src].append(des)

        res = ["JFK"]

        def dfs(src):
            if len(res) == len(tickets) +1:
                return True

            if src not in adj:
                return False

            t = adj[src]
            for i,v in enumerate(t):

                adj[src].pop(i)
                res.append(v)

                if dfs(v):
                    return True
            
                adj[src].insert(i,v)
                res.pop()

            return False










        
        dfs("JFK")
        return res