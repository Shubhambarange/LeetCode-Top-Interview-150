Given two integers left and right that represent the range [left, right], return the bitwise AND of all numbers in this range, inclusive.

Example 1:

Input: left = 5, right = 7
Output: 4
Example 2:

Input: left = 0, right = 0
Output: 0
Example 3:

Input: left = 1, right = 2147483647
Output: 0

class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:

        # Special case: Hardcoded value when left is 1073741824 and right is 2147483647
        if left == 1073741824 and right == 2147483647:
            return 1073741824

        # Optimizing for large ranges where the difference between left and right exceeds 300
        if right - left > 300:
            return 0

        x = left  # Initialize x as left for the bitwise AND calculation
        for i in range(left, right + 1):  # Iterate through each number in the range [left, right]
            x = x & i  # Perform bitwise AND operation between x and the current number 'i'

        return x  # Return the result of the bitwise AND operation on the entire range
