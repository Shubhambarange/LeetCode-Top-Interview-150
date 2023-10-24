Example 1:
Input: nums = [2,3,1,1,4]
Output: 2
Explanation: The minimum number of jumps to reach the last index is 2. Jump 1 step from index 0 to 1, then 3 steps to the last index.

Example 2:
Input: nums = [2,3,0,1,4]
Output: 2


class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        jums =0
        curr = 0
        furthest = 0 
        for i in range(0,n-1):
            furthest = max(furthest,nums[i]+i)

            if(i == curr):
                curr = furthest
                jums+=1
        return jums
