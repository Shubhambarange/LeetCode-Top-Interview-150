You are given an integer array of coins representing coins of different denominations and an integer amount representing a total amount of money.
Return the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.
You may assume that you have an infinite number of each kind of coin.

Example 1:

Input: coins = [1,2,5], amount = 11
Output: 3
Explanation: 11 = 5 + 5 + 1
Example 2:

Input: coins = [2], amount = 3
Output: -1
Example 3:

Input: coins = [1], amount = 0
Output: 0

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
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

