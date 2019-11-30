class Graph:
    def __init__(self, V, E):
        self.vertices = V
        if type(E) == list:
            self.build_adj(E)
        elif callable(E):
            self.adj = E
        else:
            raise Exception('Unknown edge type {}'.format(E))

    def build_adj(self, E):
        self.adj_dict = {}
        for edge in E:
            if type(edge) == set: # undirected
                self.add_adj(list(edge))
                self.add_adj(list(edge)[::-1])
            else: # directed
                self.add_adj(edge)

    def adj(self, s):
        return self.adj_dict[s]
    
    def add_adj(self, edge):
        u, v = edge
        if u not in self.adj_dict:
            self.adj_dict[u] = [v]
        else:
            self.adj_dict[u].append(v)
                
    def BFS(self, s):
        parent = {s: None}
        level = {s: 0}
        frontier = [s]
        level_cnt = 0
        while frontier:
            level_cnt += 1
            next = []
            for u in frontier:
                for v in self.adj(u):
                    if v not in level:
                        level[v] = level_cnt
                        parent[v] = u
                        next.append(v)
            frontier = next
        return [parent, level]

    def DFS_visit(self, s, parent = None):
        if parent is None:
            parent = {s: None}
        for u in self.adj(s):
            if u not in parent:
                parent[u] = s
                self.DFS_visit(u, parent)
        return parent


    def DFS(self):
        parent = {}
        for s in self.vertices:
            if s not in parent:
                parent[s] = None
                self.DFS_visit(s, parent)
        return parent

if __name__ == "__main__":
    g = Graph(["a","s","d","f","z","x","c","v"], [{"a","z"},{"a","s"},{"s","x"},{"x","d"}, {"x","c"},{"d","f"},{"c","f"},{"c","v"},{"f","v"}])
    print(g.adj_dict)
    print(g.BFS("s"))
    # g = Graph(["s","a"],[{"s","a"},{"a","s"}])
    print(g.DFS_visit("s"))
    print(g.DFS())
