Example 1:
Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.

Example 2:
Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.

Example 3:
Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = 0
        left = 0
        char_map = {}  # Using a dictionary to store characters and their indices.

        for right in range(len(s)):
            if s[right] in char_map and char_map[s[right]] >= left:
                res = max(res, right - left)
                left = char_map[s[right]] + 1 
            char_map[s[right]] = right 
        res = max(res, len(s) - left)

        return res
