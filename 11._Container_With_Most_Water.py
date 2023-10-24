Example 1:


Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.
Example 2:

Input: height = [1,1]
Output: 1

class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height)-1
        maxArea = 0

        while left < right:

            area = min(height[left],height[right]) * (right - left)
            maxArea = max(area,maxArea)

            if(height[left] < height[right]):
                left += 1
            else:
                right -= 1
        return maxArea
