228. Summary Ranges
You are given a sorted unique integer array nums.
A range [a,b] is the set of all integers from a to b (inclusive).
Return the smallest sorted list of ranges that cover all the numbers in the array exactly. That is, each element of nums is covered by exactly one of the ranges, and there is no integer x such that x is in one of the ranges but not in nums.

Each range [a,b] in the list should be output as:

"a->b" if a != b
"a" if a == b

Example 1:
Input: nums = [0,1,2,4,5,7]
Output: ["0->2","4->5","7"]
Explanation: The ranges are:
[0,2] --> "0->2"
[4,5] --> "4->5"
[7,7] --> "7"

Example 2:
Input: nums = [0,2,3,4,6,8,9]
Output: ["0","2->4","6","8->9"]
Explanation: The ranges are:
[0,0] --> "0"
[2,4] --> "2->4"
[6,6] --> "6"
[8,9] --> "8->9"

class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        # Initialize an empty list to store the result and get the length of the input list.
        res, n = [], len(nums)

        # If the input list is empty, return an empty result list.
        if n == 0:
            return res

        # Initialize 'a' to the first element of the input list.
        a = nums[0]

        # Iterate through the elements of the input list using a loop.
        for i in range(n):
            # Check if it's the last element or if the current element and the next element are not consecutive.
            if i == n - 1 or nums[i] + 1 != nums[i + 1]:
                # If the current range is not a single number, add the range in the form "start->end" to the result list.
                if nums[i] != a:
                    res.append(str(a) + "->" + str(nums[i]))
                else:
                    # If the current range is a single number, add only that number to the result list.
                    res.append(str(a))

                # Update 'a' to the next element to start a new range.
                if i != n - 1:
                    a = nums[i + 1]
        # Return the list of summary ranges.
        return res
