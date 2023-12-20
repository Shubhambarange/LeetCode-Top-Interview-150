Given strings s1, s2, and s3, find whether s3 is formed by an interleaving of s1 and s2.
An interleaving of two strings s and t is a configuration where s and t are divided into n and m 
substrings
 respectively, such that:

s = s1 + s2 + ... + sn
t = t1 + t2 + ... + tm
|n - m| <= 1
The interleaving is s1 + t1 + s2 + t2 + s3 + t3 + ... or t1 + s1 + t2 + s2 + t3 + s3 + ...
Note: a + b is the concatenation of strings a and b.

Example 1:
Input: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbcbcac"
Output: true
Explanation: One way to obtain s3 is:
Split s1 into s1 = "aa" + "bc" + "c", and s2 into s2 = "dbbc" + "a".
Interleaving the two splits, we get "aa" + "dbbc" + "bc" + "a" + "c" = "aadbbcbcac".
Since s3 can be obtained by interleaving s1 and s2, we return true.

Example 2:
Input: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbbaccc"
Output: false
Explanation: Notice how it is impossible to interleave s2 with any other string to obtain s3.

Example 3:
Input: s1 = "", s2 = "", s3 = ""
Output: true

class Solution:
    def check(self, s1: str, s2: str, s3: str, i, j, k) -> bool:

        if i + j == len(s3): # Nothing more to check
            return True
        if i >= len(s1): # We have consumed s1
            return s2[j:] == s3[k:]
        if j >= len(s2): # We have consumed s2
            return s1[i:] == s3[k:]
        
        if (i, j) in self.mem:
            return self.mem[(i, j)]

        if s1[i] != s3[k] and s2[j] != s3[k]:
            self.mem[(i, j)] = False
        elif s1[i] != s3[k] and s2[j] == s3[k]:
            self.mem[(i, j)] = self.check(s1, s2, s3, i, j + 1, k + 1)
        elif s1[i] == s3[k] and s2[j] != s3[k]:
            self.mem[(i, j)] = self.check(s1, s2, s3, i + 1, j, k + 1)
        if s1[i] == s3[k] and s2[j] == s3[k]:
            self.mem[(i, j)] = self.check(s1, s2, s3, i, j + 1, k + 1) or self.check(s1, s2, s3, i + 1, j, k + 1)

        return self.mem[(i, j)]
        
    
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        self.mem = {}
        if len(s1) + len(s2) != len(s3):
            return False
        return self.check(s1, s2, s3, 0, 0, 0)
