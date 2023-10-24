Example 1:

Input: numbers = [2,7,11,15], target = 9
Output: [1,2]
Explanation: The sum of 2 and 7 is 9. Therefore, index1 = 1, index2 = 2. We return [1, 2].
Example 2:

Input: numbers = [2,3,4], target = 6
Output: [1,3]
Explanation: The sum of 2 and 4 is 6. Therefore index1 = 1, index2 = 3. We return [1, 3].
Example 3:

Input: numbers = [-1,0], target = -1
Output: [1,2]
Explanation: The sum of -1 and 0 is -1. Therefore index1 = 1, index2 = 2. We return [1, 2].


class Solution {
public:
    vector<int> twoSum(vector<int>& numbers, int target) {
        vector<int> res;
        int start = 0;
        int end = numbers.size() - 1; // Initialize 'end' to the last index

        while (start < end) {
            int sum = numbers[start] + numbers[end];
            if (sum == target) {
                // Add 1 to both indices since indices are 1-based in the problem statement
                res.push_back(start + 1);
                res.push_back(end + 1);
                return res;
            } else if (sum > target) {
                end--;
            } else {
                start++;
            }
        }

        // Return an empty vector if no solution is found
        return res;
    }
};
