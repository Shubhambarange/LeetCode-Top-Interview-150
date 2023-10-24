Example 1:
Input: s = "the sky is blue"
Output: "blue is sky the"
  
Example 2:
Input: s = "  hello world  "
Output: "world hello"
Explanation: Your reversed string should not contain leading or trailing spaces.

Example 3:
Input: s = "a good   example"
Output: "example good a"
Explanation: You need to reduce multiple spaces between two words to a single space in the reversed string.
 

class Solution {
public:
    string reverseWords(string s) 
    {
        int i=0,j=0,flag=0;
        while(s[i]==' ')
            i++;
        s=s.substr(i,s.size());
        reverse(s.begin(),s.end());
        
        i=0;
        while(s[i]==' ')
            i++;
        s=s.substr(i,s.size());
        reverse(s.begin(),s.end());
        
        
        i=0;
        while(j!=s.size())
        {
            if(s[j]!=' ')
            {
                s[i]=s[j];
                i++;
                j++;
                flag=0;
            }
            else if(s[j]==' ' && flag==0)
            {
                s[i]=' ';
                i++;
                j++;
                flag=1;
            }
            else
            {
                
                j++;
            }
        }
        s=s.substr(0,i);
        //cout<<s;
        
        int beg=0;
        for(int i=0;i<s.size();i++)
        {
            if(s[i]==32)
            {
                reverse(s.begin()+beg,s.begin()+i);
                beg=i+1;
            }
        }
        reverse(s.begin()+beg,s.end());
        //cout<<s;
        reverse(s.begin(),s.end());
        return s;
    }
};
