class UnionFind:
    def __init__(self,n):
        self.n = n
        self.parent = list(range(n+1))
        self.size = [1]*(n+1)
    def find(self,node):
        if self.parent[node] != node:
            self.parent[node] = self.find(self.parent[node])
        return self.parent[node]
    def union(self,u,v):
        pu = self.find(u)
        pv = self.find(v)
        if pu == pv:
            return False
        self.n -= 1
        if self.size[pu] < self.size[pv]:
            pu , pv = pv, pu
        self.size[pu] += self.size[pv]
        self.parent[pv] = pu
        return True
    def isConnected(self):
        return self.n == 1

class Solution:
    def findCriticalAndPseudoCriticalEdges(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        for i , e in enumerate(edges):
            e.append(i)
        edges.sort(key = lambda e : e[2])

        def findMST(idx,include):
            uf = UnionFind(n)
            wt = 0
            if include:
                uf.union(edges[idx][0], edges[idx][1])
                wt += edges[idx][2]
            for i,e in enumerate(edges):
                if i == idx:
                    continue
                if uf.union(e[0],e[1]):
                    wt += e[2]
            return wt if uf.isConnected() else float('inf')

        mst_wt = findMST(-1,False)
        critical , pseudo = [] , []
        for i , e in enumerate(edges):
            if mst_wt < findMST(i,False):
                critical.append(e[3])
            elif mst_wt == findMST(i,True):
                pseudo.append(e[3])
        return [critical,pseudo]
