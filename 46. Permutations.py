Given an array nums of distinct integers, return all the possible permutations. You can return the answer in any order.
Example 1:

Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]

Example 2:
Input: nums = [0,1]
Output: [[0,1],[1,0]]

Example 3:
Input: nums = [1]
Output: [[1]]

from typing import List

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def backtrack(reslist, templist, nums):
            if len(templist) == len(nums):
                reslist.append(templist[:])
                return
            
            for number in nums:
                if number not in templist:  # Check if the number is not already in the templist
                    templist.append(number)
                    backtrack(reslist, templist, nums)
                    templist.pop()

        reslist = []
        backtrack(reslist, [], nums)
        return reslist