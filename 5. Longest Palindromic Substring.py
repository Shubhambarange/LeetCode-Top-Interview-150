Given a string s, return the longest palindromic substring in s.

Example 1:
Input: s = "babad"
Output: "bab"
Explanation: "aba" is also a valid answer.
  
Example 2:
Input: s = "cbbd"
Output: "bb"
class Solution:
    
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        if n < 2:
            return s
        i = 0
        mx_p = s[0]
        while i < n:
            cntr = s[i]
            for r in range(i+1, n):
                if s[i] == s[r]:
                    cntr += s[r]
                else: break

            max_pal_len = 2*min(i, n-i-len(cntr))+len(cntr)
            if max_pal_len < len(mx_p):
                return mx_p

            mx_p = cntr if len(cntr) > len(mx_p) else mx_p
            li, ri = i-1, i+len(cntr)
            while li >= 0 and ri < n and s[li] == s[ri]:
                if ri-li+1 > len(mx_p):
                    mx_p = s[li:ri+1]
                li -= 1
                ri += 1
            i += len(cntr)
        return mx_p
            
        

