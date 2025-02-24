import collections
from typing import List
class Solution:
    def mostProfitablePath(self, edges: List[List[int]], bob: int, amount: List[int]) -> int:
        adj = collections.defaultdict(list)
        for v1, v2 in edges:
            adj[v1].append(v2)
            adj[v2].append(v1)

        # Bob simulation - DFS
        bob_times = {}  # node on root path -> time visited

        def dfs(src, prev, time):
            if src == 0:
                bob_times[src] = time
                return True
            for nei in adj[src]:
                if nei == prev:
                    continue
                if dfs(nei, src, time + 1):
                    bob_times[src] = time
                    return True
            return False

        dfs(bob, -1, 0)

        # Alice simulation - BFS
        q = collections.deque([(0, 0, -1, amount[0])])  # (node,time,parent,total profit)
        res = float('-inf')
        while q:
            node, time, parent, profit = q.popleft()
            for nei in adj[node]:
                if nei == parent:
                    continue
                nei_profit = amount[nei]
                nei_time = time + 1
                if nei in bob_times:
                    if nei_time > bob_times[nei]:
                        nei_profit = 0
                    if nei_time == bob_times[nei]:
                        nei_profit = nei_profit // 2
                q.append((nei, nei_time, node, profit + nei_profit))
                if len(adj[nei]) == 1:
                    res = max(res, profit + nei_profit)
        return res

if __name__ == "__main__":
    edges = [[0, 1], [1, 2], [1, 3], [3, 4]]
    bob = 3
    amount = [-2, 4, 2, -4, 6]
    solution = Solution()
    result = solution.mostProfitablePath(edges, bob, amount)
    expected = 6
    print("Pass" if result == expected else f"Expected {expected}, but got {result}")
