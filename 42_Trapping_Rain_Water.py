Example 1:
Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped.

Example 2:
Input: height = [4,2,0,3,2,5]
Output: 9

class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        lmax = [0] * n
        rmax = [0] * n

        lmax[0] = height[0]
        rmax[n - 1] = height[n - 1]

        for i in range(1, n):
            lmax[i] = max(lmax[i - 1], height[i])

        for i in range(n - 2, -1, -1):
            rmax[i] = max(rmax[i + 1], height[i])

        water = 0

        for i in range(1, n - 1):
            water += min(lmax[i], rmax[i]) - height[i]

        return water
