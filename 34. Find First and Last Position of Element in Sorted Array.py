Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given target value.
If target is not found in the array, return [-1, -1].
You must write an algorithm with O(log n) runtime complexity.

Example 1:
Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]

Example 2:
Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]

Example 3:
Input: nums = [], target = 0
Output: [-1,-1]


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        # Function to find the leftmost occurrence of the target element in the sorted array
        def findleftBound(nums, target):
            index = -1
            low = 0
            high = len(nums) - 1

            while low <= high:
                mid = low + (high - low) // 2
                if nums[mid] == target:
                    index = mid
                    high = mid - 1  # Move towards the left for further search
                elif nums[mid] < target:
                    low = mid + 1
                else:
                    high = mid - 1
            return index

        # Function to find the rightmost occurrence of the target element in the sorted array
        def findrightBound(nums, target):
            index = -1
            low = 0
            high = len(nums) - 1

            while low <= high:
                mid = low + (high - low) // 2
                if nums[mid] == target:
                    index = mid
                    low = mid + 1  # Move towards the right for further search
                elif nums[mid] < target:
                    low = mid + 1
                else:
                    high = mid - 1
            return index

        # Find both left and right bounds for the target element
        left = findleftBound(nums, target)
        right = findrightBound(nums, target)

        return [left, right]  # Return the indices of leftmost and rightmost occurrences
