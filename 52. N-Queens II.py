The n-queens puzzle is the problem of placing n queens on an n x n chessboard such that no two queens attack each other.
Given an integer n, return the number of distinct solutions to the n-queens puzzle.

Example 1:
Input: n = 4
Output: 2
Explanation: There are two distinct solutions to the 4-queens puzzle as shown.

Example 2:
Input: n = 1
Output: 1

class Solution:
    def totalNQueens(self, n: int) -> int:
        # Initialize sets to keep track of occupied columns, positive diagonals, and negative diagonals
        col = set()
        posDiag = set()  # (row + col)
        negDiag = set()  # (row - col)

        res = 0  # Counter for the total number of solutions

        def backtrack(r):
            if r == n:  # If all queens are placed successfully, increment the result count
                nonlocal res
                res += 1
                return

            for c in range(n):  # Iterate through each column in the current row
                if c in col or (r + c) in posDiag or (r - c) in negDiag:
                    # Check if the current column or its diagonals are already occupied by other queens
                    continue  # If so, move to the next column

                # Mark the column and diagonals occupied by the current queen
                col.add(c)
                posDiag.add((r + c))
                negDiag.add((r - c))

                # Recursively move to the next row to place the next queen
                backtrack(r + 1)

                # Remove the queen and free up the column and diagonals for the next iteration
                col.remove(c)
                posDiag.remove(r + c)
                negDiag.remove(r - c)

        backtrack(0)  # Start the backtracking process from the first row
        return res  # Return the total number of solutions found
