Given a string s and a dictionary of strings wordDict, return true if s can be segmented into a space-separated sequence of one or more dictionary words.
Note that the same word in the dictionary may be reused multiple times in the segmentation.
 
Example 1:

Input: s = "leetcode", wordDict = ["leet","code"]
Output: true
Explanation: Return true because "leetcode" can be segmented as "leet code".

Example 2:

Input: s = "applepenapple", wordDict = ["apple","pen"]
Output: true
Explanation: Return true because "applepenapple" can be segmented as "apple pen apple".
Note that you are allowed to reuse a dictionary word.

Example 3:

Input: s = "catsandog", wordDict = ["cats","dog","sand","and","cat"]
Output: false

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # Convert wordDict into a set for faster lookup
        word_set = set(wordDict)
        
        # Initialize a set to keep track of possible word breaks
        dp = {0}
        
        # Iterate through the string
        for j in range(1, len(s) + 1):
            # Iterate through the current elements in dp (copying the set to avoid modifying it while iterating)
            for i in dp.copy():
                # Check if substring from i to j exists in the word_set
                if s[i:j] in word_set:
                    # If it exists, add index j to dp to mark that a word break is possible up to index j
                    dp.add(j)
        
        # Check if the length of the string is present in dp,
        # indicating that the entire string can be broken into words from the dictionary
        return len(s) in dp
