Given an m x n board of characters and a list of strings words, return all words on the board.

Each word must be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once in a word.

Example 1:
Input: board = [["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]], words = ["oath","pea","eat","rain"]
Output: ["eat","oath"]

Example 2:
Input: board = [["a","b"],["c","d"]], words = ["abcb"]
Output: []


class Node:
    def __init__(self):
        self.children = {}
        self.end = False


class Trie:
    def __init__(self):
        self.root = Node()

    def insert(self, word):
        node = self.root
        for i in word:
            if i not in node.children:
                node.children[i] = Node()
            node = node.children[i]
        node.end = True


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        row, col = len(board), len(board[0])
        trie = Trie()
        for word in words:
            trie.insert(word)

        def dfs(i, j, node, path):
            if i < 0 or i >= row or j < 0 or j >= col or board[i][j] == '#':
                return

            char = board[i][j]
            if char not in node.children:
                return

            path += char
            node = node.children[char]

            if node.end:
                result.append(path)
                node.end = False

            board[i][j] = '#'
            dfs(i + 1, j, node, path)
            dfs(i - 1, j, node, path)
            dfs(i, j + 1, node, path)
            dfs(i, j - 1, node, path)
            board[i][j] = char
        result = []
        for i in range(row):
            for j in range(col):
                dfs(i, j, trie.root, "")

        return result
