class UnionFind:
    def __init__(self, n: int):
        self.parent = list(range(n))
        self.size = [1] * n
        self.max_area = 0

    def find(self, x: int):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    def union(self, a: int, b: int) -> None:
        root_a = self.find(a)
        root_b = self.find(b)

        if root_a == root_b:
            return

        if self.size[root_a] < self.size[root_b]:
            root_a, root_b = root_b, root_a
        self.parent[root_b] = root_a
        self.size[root_a] += self.size[root_b]

        self.max_area = max(self.max_area, self.size[root_a])

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        uf = UnionFind(rows * cols)

        for r in range(rows):
            for c in range(cols):
                if grid[r][c]:
                    uf.max_area = max(uf.max_area, 1)
                    idx = r * cols + c
                    for x, y in [(0, 1), (1, 0)]:
                        nr, nc = r + x, c + y
                        if not (0 <= nr < rows and 0 <= nc < cols): continue
                        if not grid[nr][nc]: continue
                        n_idx = nr * cols + nc
                        uf.union(idx, n_idx)
        return uf.max_area
                    



        