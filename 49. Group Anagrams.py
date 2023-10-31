Example 1:
Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

Example 2:
Input: strs = [""]
Output: [[""]]

Example 3:
Input: strs = ["a"]
Output: [["a"]]

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        def getFrequencyString(s):
            freq = [0]*26
            for c in s:
                freq[ord(c) - ord('a')] += 1
            
            frequencyString = ""
            c = 'a'
            for i in freq:
                frequencyString += c
                frequencyString += str(i)
                c = chr(ord(c) + 1)
            return frequencyString 

        if strs is None or len(strs) == 0:
            return []

        frequencyStringsMap = {}

        for s in strs:
            frequencyString = getFrequencyString(s)

            if (frequencyString in frequencyStringsMap):
                frequencyStringsMap[frequencyString].append(s)
            else:
                frequencyStringsMap[frequencyString] = [s]

        return list(frequencyStringsMap.values())
