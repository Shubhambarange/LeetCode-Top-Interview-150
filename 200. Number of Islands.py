Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.

An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

Example 1:
Input: grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
Output: 1

Example 2:
Input: grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
Output: 3

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        self.grid = grid
        self.m = len(grid)
        self.n = len(grid[0])
        self.count = 0

        for i in range(self.m):
            for j in range(self.n):
                if self.grid[i][j] == '1':
                    self.traverse(i, j)
                    self.count += 1
        return self.count

    def traverse(self, i: int, j: int) -> None:
        if i < 0 or j < 0 or i >= self.m or j >= self.n or self.grid[i][j] != '1':
            return
        self.grid[i][j] = '2'  # mark as visited
        self.traverse(i - 1, j)  # up
        self.traverse(i, j + 1)  # right
        self.traverse(i + 1, j)  # down
        self.traverse(i, j - 1)  # left
