Example 1:

Input: s = "PAYPALISHIRING", numRows = 3
Output: "PAHNAPLSIIGYIR"

Example 2:
Input: s = "PAYPALISHIRING", numRows = 4
Output: "PINALSIGYAHRPI"
Explanation:
P     I    N
A   L S  I G
Y A   H R
P     I

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s        
        res = ""
        for r in range(numRows):
            increment = 2*(numRows-1)
            for i in range(r,len(s),increment):
                res += s[i]
                if(r>0 and r<numRows -1 and i + increment -2 *r < len(s)):
                    res += s[i + increment - 2 *r]
        return res
