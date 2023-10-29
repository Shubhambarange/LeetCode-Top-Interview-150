Example 1:
Input: ransomNote = "a", magazine = "b"
Output: false
  
Example 2:
Input: ransomNote = "aa", magazine = "ab"
Output: false
  
Example 3:
Input: ransomNote = "aa", magazine = "aab"
Output: true

  
class Solution {
public:
   bool canConstruct(string ransomNote, string magazine) {
        vector<int> charCount(26, 0); // Assuming only lowercase letters (a-z)

        // Count characters in magazine
        for (char ch : magazine) {
            charCount[ch - 'a']++;
        }

        // Check if we can construct the ransomNote
        for (char ch : ransomNote) {
            if (charCount[ch - 'a'] > 0) {
                charCount[ch - 'a']--;
            } else {
                return false;
            }
        }

        return true;
    }
};
