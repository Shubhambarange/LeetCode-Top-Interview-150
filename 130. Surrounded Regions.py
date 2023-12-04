Given an m x n matrix board containing 'X' and 'O', capture all regions that are 4-directionally surrounded by 'X'.
A region is captured by flipping all 'O's into 'X's in that surrounded region.

Example 1:
Input: board = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]
Output: [["X","X","X","X"],["X","X","X","X"],["X","X","X","X"],["X","O","X","X"]]
Explanation: Notice that an 'O' should not be flipped if:
- It is on the border, or
- It is adjacent to an 'O' that should not be flipped.
The bottom 'O' is on the border, so it is not flipped.
The other three 'O' form a surrounded region, so they are flipped.

Example 2:
Input: board = [["X"]]
Output: [["X"]]

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        m = len(board[0])
        n = len(board)

        q = collections.deque()

        # First row
        for i in range(m):
            if board[0][i] == "O":
                q.append((0, i))
                board[0][i] = "F"

        # Last row
        if n > 1:
            for i in range(m):
                if board[n-1][i] == "O":
                    q.append((n-1, i))
                    board[n-1][i] = "F"

        # First column
        for i in range(1, n-1):
            if board[i][0] == "O":
                q.append((i, 0))
                board[i][0] = "F"

        # Last column
        if m > 1:
            for i in range(1, n-1):
                if board[i][m-1] == "O":
                    q.append((i, m-1))
                    board[i][m-1] = "F"

        directions = [[-1, 0], [1, 0], [0, 1], [0, -1]]

        while q:
            curr = q.popleft()

            for direction in directions:
                newRow = curr[0] + direction[0]
                newCol = curr[1] + direction[1]

                if (
                    (newRow >= 0 and newRow < n) and
                    (newCol >= 0 and newCol < m) and
                    board[newRow][newCol] == "O"
                ):
                    q.append((newRow, newCol))
                    board[newRow][newCol] = "F"


        for i in range(n):
            for j in range(m):
                if board[i][j] == "O":
                    board[i][j] = "X"
                elif board[i][j] == "F":
                    board[i][j] = "O"
        
        
