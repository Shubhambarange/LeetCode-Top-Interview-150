Example 1:
Input: s = "anagram", t = "nagaram"
Output: true

Example 2:
Input: s = "rat", t = "car"
Output: false


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        dict1 = Counter(s) # Make the dictionary of s
        dict2 = Counter(t) # Make the dictionary of t
        for i in range(len(dict1)): 
            if dict1 == dict2: # if both dictionaries have the equal key: value pair then it returns true
                return True
            return False
