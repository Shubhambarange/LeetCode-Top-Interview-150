Example 1:

Input: nums = [3,2,3]
Output: 3
Example 2:

Input: nums = [2,2,1,1,1,2,2]
Output: 2


class Solution:
    def majorityElement(self, nums: List[int]) -> int:

        count =0
        candidate =0
        for num in nums:
            if count ==0:
                 candidate = num
            if candidate == num:
                count+=1
            else:
                count-=1
        return candidate
