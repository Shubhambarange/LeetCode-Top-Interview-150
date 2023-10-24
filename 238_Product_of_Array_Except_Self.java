Example 1:

Input: nums = [1,2,3,4]
Output: [24,12,8,6]
  
Example 2:
Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]
 
class Solution {
    public int[] productExceptSelf(int[] nums) {
        int n = nums.length;
        int [] res = new int[n];
        int productOfAllBeforeCurrent = 1;
        int productOfAllAftereCurrent = 1;

        for(int i =0; i<n; i++){
            res[i] = productOfAllBeforeCurrent;
            productOfAllBeforeCurrent *= nums[i];
        }
        for(int i = n-1; i >= 0; i--){
            res[i] *= productOfAllAftereCurrent;
            productOfAllAftereCurrent *= nums[i];
        }
        return res;
    }
}
