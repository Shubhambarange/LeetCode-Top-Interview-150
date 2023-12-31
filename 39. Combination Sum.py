Given an array of distinct integers candidates and a target integer target, return a list of all unique combinations of candidates where the chosen numbers sum to target. You may return the combinations in any order.

The same number may be chosen from candidates an unlimited number of times. Two combinations are unique if the 
frequency
 of at least one of the chosen numbers is different.

The test cases are generated such that the number of unique combinations that sum up to target is less than 150 combinations for the given input.

Example 1:
Input: candidates = [2,3,6,7], target = 7
Output: [[2,2,3],[7]]
Explanation:
2 and 3 are candidates, and 2 + 2 + 3 = 7. Note that 2 can be used multiple times.
7 is a candidate, and 7 = 7.
These are the only two combinations.
  
Example 2:
Input: candidates = [2,3,5], target = 8
Output: [[2,2,2,2],[2,3,3],[3,5]]

Example 3:
Input: candidates = [2], target = 1
Output: []


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []

        # Define a depth-first search (DFS) function to find combinations
        def dfs(i, cur, total):
            # If the current total equals the target, add the current combination to the result
            if total == target:
                res.append(cur.copy())
                return 
            
            # If the index exceeds the candidates' length or if the total exceeds the target, stop this branch of the search
            if i >= len(candidates) or total > target:
                return
            
            # Choose the current candidate and proceed recursively
            cur.append(candidates[i])  # Choose the candidate at index i
            dfs(i, cur, total + candidates[i])  # Continue to explore combinations with the chosen candidate
            cur.pop()  # Backtrack: remove the last candidate to explore other possibilities
            
            # Skip to the next candidate and continue exploring combinations
            dfs(i + 1, cur, total)

        # Start DFS with initial parameters: index i = 0, an empty combination, and total sum = 0
        dfs(0, [], 0)
        
        return res  # Return the list of combinations that sum up to the target
