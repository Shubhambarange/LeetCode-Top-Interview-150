Example 1:
Input: s = "abc", t = "ahbgdc"
Output: true
  
Example 2:
Input: s = "axc", t = "ahbgdc"
Output: false

  
class Solution {
public:
    bool isSubsequence(string s, string t) {
        int subsequens = 0;
        for(int i=0; i<t.length();i++){
            if(subsequens <= s.length()-1){
                if(s[subsequens] == t[i]){
                    subsequens+=1;
                }
            }

        }
        return (subsequens == s.length() );
    }
};
