Example 1:

Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.
Example 2:

Input: s = "race a car"
Output: false
Explanation: "raceacar" is not a palindrome.
Example 3:

Input: s = " "
Output: true
Explanation: s is an empty string "" after removing non-alphanumeric characters.
Since an empty string reads the same forward and backward, it is a palindrome.

class Solution {
public:
    bool isPalindrome(string s) {
        if(s.length() <= 1)
            return true;
        int start = 0, end = s.length()-1;
        while(start <end) {
        while(start < end && !isalnum(s[start]))
            start++;
        while(start < end && !isalnum(s[end]))
            end--;
        if(start < end && tolower(s[start]) != tolower(s[end]))
            return false;
        start++;
        end--;
        }
        return true;
    }
    
};
