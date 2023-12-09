Given an m x n grid of characters board and a string word, return true if word exists in the grid.
The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once.

Example 1:
Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
Output: true

Example 2:
Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "SEE"
Output: true

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def dfs(i, j, letter_count):
            if (letter_count == len(word)):
                return True

            if (i < 0 or j < 0 or i >= len(board) or j >= len(board[0]) or board[i][j] != word[letter_count]):
                return

            temp = board[i][j]
            board[i][j] = "."
                           
            found = (dfs(i + 1, j, letter_count + 1) or # checks the top letter
                     dfs(i - 1, j, letter_count + 1) or # checks the bottom letter
                     dfs(i, j + 1, letter_count + 1) or # checks the right letter
                     dfs(i, j - 1, letter_count + 1))   # checks the left letter
            board[i][j] = temp
            return found
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0]:
                    if dfs(i, j, 0):
                        return True

        return False
