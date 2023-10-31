Example 1:
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

Example 2:
Input: nums = [3,2,4], target = 6
Output: [1,2]

Example 3:
Input: nums = [3,3], target = 6
Output: [0,1]


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
       n = len(nums)
       map = {}

       for i in range(0,n):
           remaining = target - nums[i]

           if remaining in map:
               return [map[remaining],i]       
           map[nums[i]]= i
       
        
        
