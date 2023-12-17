Given an integer array nums, return the length of the longest strictly increasing 
subsequence
.
Example 1:

Input: nums = [10,9,2,5,3,7,101,18]
Output: 4
Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4.

Example 2:

Input: nums = [0,1,0,3,2,3]
Output: 4

Example 3:

Input: nums = [7,7,7,7,7,7,7]
Output: 1

class CoinChange:
    def coinChange(self, coins, amount):
        if amount < 1:
            return 0

        # Create DP array
        min_coins_dp = [float('inf')] * (amount + 1)
        min_coins_dp[0] = 0

        for i in range(1, amount + 1):
            for coin in coins:
                if coin <= i and min_coins_dp[i - coin] != float('inf'):
                    min_coins_dp[i] = min(min_coins_dp[i], 1 + min_coins_dp[i - coin])

        return min_coins_dp[amount] if min_coins_dp[amount] != float('inf') else -1
