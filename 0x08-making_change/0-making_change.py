#!/usr/bin/python3
"""
a pile of coins of different values,
determine the fewest number of coins
needed to meet a given amount total.
"""


def makeChange(coins, total):
    if total <= 0:
        return 0

    # Initialize the dp array
    dp = [float('inf')] * (total + 1)
    dp[0] = 0  # No coins are needed to make total of 0

    # Fill the dp array
    for amount in range(1, total + 1):
        for coin in coins:
            if coin <= amount:
                dp[amount] = min(dp[amount], dp[amount - coin] + 1)

    return dp[total] if dp[total] != float('inf') else -1
