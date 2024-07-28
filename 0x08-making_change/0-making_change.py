#!/usr/bin/python3
"""
a pile of coins of different values,
determine the fewest number of coins
needed to meet a given amount total.
"""


def makeChange(coins, total):
    """
    Determine the fewest number of coins needed to meet a given amount total.


    Args:
        coins (list): A list of coin denominations.
        total (int): The total amount of money to make change for.

    Returns:
        int: The fewest number of coins
        needed to make the total, or -1 if it is not possible.
    """
    if total <= 0:
        return 0

    coins.sort()

    dp = [float('inf')] * (total + 1)
    dp[0] = 0

    for amount in range(1, total + 1):
        for coin in coins:
            if coin <= amount:
                dp[amount] = min(dp[amount], dp[amount - coin] + 1)

                return dp[total] if dp[total] != float('inf') else -1
