class BipartiteMatching:
    def __init__(self, v: int):
        """
        :param v: 頂点数
        """
        self.v = v
        self.g = [[] for _ in range(v)]
        self.match = [-1] * v
        self.used = [False] * v

    def add_edge(self, u, v):
        self.g[u].append(v)
        self.g[v].append(u)

    def dfs(self, v) -> bool:
        self.used[v] = True
        for i in range(len(self.g[v])):
            u = self.g[v][i]
            w = self.match[u]

            if w < 0 or (not self.used[w] and self.dfs(w)):
                self.match[u] = v
                self.match[v] = u
                return True

        return False

    def maximum_matching(self) -> int:
        res = 0
        self.match = [-1] * self.v
        for i in range(self.v):
            if self.match[i] < 0:
                self.used = [False] * self.v
                if self.dfs(i):
                    res += 1
        return res
