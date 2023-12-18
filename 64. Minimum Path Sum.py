Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right, which minimizes the sum of all numbers along its path.
Note: You can only move either down or right at any point in time.

Example 1:
Input: grid = [[1,3,1],[1,5,1],[4,2,1]]
Output: 7
Explanation: Because the path 1 → 3 → 1 → 1 → 1 minimizes the sum.

Example 2:
Input: grid = [[1,2,3],[4,5,6]]
Output: 12

class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:

# Tabulation
        n=len(grid)
        m=len(grid[0])
        dp=[[0 for i in range(m)] for j in range(n)]

        for i in range(n):
            for j in range(m):
                if i==0 and j==0:
                    dp[i][j]=grid[0][0]
                else:
                    up=grid[i][j]
                    if i >0:
                        up+=dp[i-1][j]
                    else:
                        up+=1e9
                    left=grid[i][j]
                    if j>0:
                        left+=dp[i][j-1]
                    else:
                        left+=1e9
                    dp[i][j]=min(up,left)
        return dp[n-1][m-1]
            
        

#Recursion with memoization
        n=len(grid)
        m=len(grid[0])
        dp=[[-1 for i in range(m)] for j in range(n)]
        def func(row,col):
            if row==0 and col==0:
                return grid[row][col]
            if row<0 or col<0:
                return 1e9
            if dp[row][col]!=-1:
                return dp[row][col]
            up=grid[row][col]+func(row-1,col)
            left=grid[row][col]+func(row,col-1)
            dp[row][col]=min(up,left)
            return dp[row][col]
        return func(n-1,m-1)



#Recursion
        n=len(grid)
        m=len(grid[0])
        def func(row,col):
            if row==0 and col==0:
                return grid[row][col]

            if row<0 or col<0:
                return 1e9
            up=grid[row][col]+func(row-1,col)
            left=grid[row][col]+func(row,col-1)
            return min(up,left)
        return func(n-1,m-1)

        
        
