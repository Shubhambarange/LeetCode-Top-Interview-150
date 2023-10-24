Level -- HARD 	

Example 1:
Input: s = "ADOBECODEBANC", t = "ABC"
Output: "BANC"
Explanation: The minimum window substring "BANC" includes 'A', 'B', and 'C' from string t.
  
Example 2:
Input: s = "a", t = "a"
Output: "a"
Explanation: The entire string s is the minimum window.
  
Example 3:
Input: s = "a", t = "aa"
Output: ""
Explanation: Both 'a's from t must be included in the window.
Since the largest window of s only has one 'a', return empty string.

class Solution {
public:
    string minWindow(string s, string t) {
        if(s.length() == 0 || t.length() == 0 || s.length() < t.length()) return "";

        vector<int> v(256,0);
        for(int i = 0; i<t.length(); i++){
            v[t[i]]++;
        }

        int start = 0 , end = 0 , ans_start = 0;
        int minlength = INT_MAX;
        int count = 0 ;

        while(end<s.length()){
            if(v[s[end]] > 0) count++;

            v[s[end]]--;

            while(count == (int)t.length()){

                if(minlength > end - start + 1 ){
                    minlength = end - start + 1;
                    ans_start = start;
                }

                v[s[start]]++;

                if(v[s[start]] > 0){
                    count--;
                }

                start++;
            }
            end++;
        }
        if(minlength == INT_MAX) // no string Found
            return  "";
        
        return s.substr(ans_start, minlength);
        
    }
    
};
