Given an integer array nums where every element appears three times except for one, which appears exactly once. Find the single element and return it.

You must implement a solution with a linear runtime complexity and use only constant extra space.
  
Example 1:

Input: nums = [2,2,3,2]
Output: 3
Example 2:

Input: nums = [0,1,0,1,0,1,99]
Output: 99

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        map_count = {}
        for i in range(len(nums)):
            if nums[i] not in map_count:
                map_count[nums[i]]=1
            else:
                map_count[nums[i]]+=1
        for key, value in map_count.items():
            if value == 1:
                return key
