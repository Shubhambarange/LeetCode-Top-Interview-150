Given two strings word1 and word2, return the minimum number of operations required to convert word1 to word2.
You have the following three operations permitted on a word:
Insert a character
Delete a character
Replace a character
 
Example 1:
Input: word1 = "horse", word2 = "ros"
Output: 3
Explanation: 
horse -> rorse (replace 'h' with 'r')
rorse -> rose (remove 'r')
rose -> ros (remove 'e')
Example 2:

Input: word1 = "intention", word2 = "execution"
Output: 5
Explanation: 
intention -> inention (remove 't')
inention -> enention (replace 'i' with 'e')
enention -> exention (replace 'n' with 'x')
exention -> exection (replace 'n' with 'c')
exection -> execution (insert 'u')


class Solution:
    def minDistance(self, word1: str, word2: str) -> int:

        def strMatch(word1, word2, i, j, dp):
            # BASE CASE
            if i < 0:
                return j+1
            if j < 0:
                return i+1
            
            if dp[i][j] != -1:
                return dp[i][j]
                
            # IF THE CHARACTER MATCHES THERE IS NO NEED TO DO ANYTHING.
            if word1[i] == word2[j]:
                dp[i][j] = strMatch(word1, word2, i-1, j-1, dp)
                return dp[i][j]
                
            insert = strMatch(word1, word2, i, j-1, dp) + 1
            delete = strMatch(word1, word2, i-1, j, dp) + 1
            replace = strMatch(word1, word2, i-1, j-1, dp) + 1

            dp[i][j] = min(insert, delete, replace)
            
            return dp[i][j]
            
        n = len(word1)
        m = len(word2)
        dp = [[-1]*m for _ in range(n)]
        return strMatch(word1, word2, n-1, m-1, dp)
