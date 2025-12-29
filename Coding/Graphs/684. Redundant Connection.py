class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        # union-find approach

        parent = {i:-1 for i in range(1, len(edges)+1)}
        # finds the absolute parent of node:u
        def find(u):
            if parent[u] != -1:
                parent[u] = find(parent[u])
                return parent[u]
            else:
                return u
        
        # union operation
        def union(u,v):
            parent_u = find(u)
            parent_v = find(v)

            if parent_u == parent_v:
                return True # adding this edge leads to cycle
            else:
                # combine u and v -> combine parents of u and v
                parent[parent_u] = parent_v
                return False # adding this edge leads to no cycle
        
        for i in edges:
            if union(i[0],i[1]):
                return i
