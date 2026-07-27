class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        # adj list
        adj = {i:[] for i in range(n)}

        for parent, child in edges:
            adj[parent].append(child)
            adj[child].append(parent)

        def dfs(cur, parent):
            time = 0
            for child in adj[cur]:
                if child == parent: continue
                childTime = dfs(child, cur)
                if childTime or hasApple[child]:
                    time += 2 + childTime
            return time

        return dfs(0, -1)