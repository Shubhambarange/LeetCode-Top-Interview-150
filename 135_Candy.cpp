Example 1:

Input: ratings = [1,0,2]
Output: 5
Explanation: You can allocate to the first, second and third child with 2, 1, 2 candies respectively.
Example 2:

Input: ratings = [1,2,2]
Output: 4
Explanation: You can allocate to the first, second and third child with 1, 2, 1 candies respectively.
The third child gets 1 candy because it satisfies the above two conditions.

class Solution {
public:
    int candy(vector<int>& ratings) {
        int n = ratings.size();
        vector<int> c(n,1);

        if(n==1){
            return 1;
        }
        // left to right 
        for(int i =1;i<n;i++)
        {
            if(ratings[i] > ratings[i-1] &&  c[i] <= c[i-1]){
                c[i] = c[i-1] + 1;
                
            }
        }
         // right to left 
        for(int i =n-2;i>=0;i--)
        {
            if(ratings[i] > ratings[i+1] &&  c[i] <= c[i+1]){
                c[i] = c[i+1] + 1;}
        }

        int total = 0;

        for(int i=0;i<n;i++){
            total +=c[i];
        }
        return total;
    }
};
