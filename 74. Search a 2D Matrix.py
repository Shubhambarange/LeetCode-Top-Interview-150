You are given an m x n integer matrix matrix with the following two properties:

Each row is sorted in non-decreasing order.
The first integer of each row is greater than the last integer of the previous row.
Given an integer target, return true if target is in matrix or false otherwise.

You must write a solution in O(log(m * n)) time complexity.
  
Example 1:
Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
Output: true

Example 2:
Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13
Output: false

from typing import List

class Solution:
    def searchPotentialRow(self, matrix: List[List[int]], target: int) -> int:
        low = 0 
        high = len(matrix) - 1 

        while low <= high:
            mid = low + (high - low) // 2

            if matrix[mid][0] <= target <= matrix[mid][-1]:  # Check against the last element of the row
                return mid

            elif matrix[mid][0] < target: 
                low = mid + 1
            else:  # Adjust the condition to check the upper bound
                high = mid - 1
        return -1

    def binarySearchOverRow(self, rowIdx: int, matrix: List[List[int]], target: int) -> bool:
        low = 0
        high = len(matrix[rowIdx]) - 1

        while low <= high:
            mid = low + (high - low) // 2

            if matrix[rowIdx][mid] == target:
                return True
            elif matrix[rowIdx][mid] > target:
                high = mid - 1
            else:
                low = mid + 1
        return False

    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rowIdx = self.searchPotentialRow(matrix, target)
        if rowIdx != -1:
            return self.binarySearchOverRow(rowIdx, matrix, target)
        return False
