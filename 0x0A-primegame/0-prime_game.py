#!/usr/bin/python3
"""Prime Game"""


def isWinner(x, nums):
    """
    Determine the winner of a prime-number game played over x rounds
    Parameters:
    x (int): The number of rounds to be played.
    nums (list of int): A list of integers where each integer n
    represents the range of numbers from 1 to n for each round.
    Returns:
    str: The name of the player who won the most rounds ("Maria" or "Ben").
         If there is a tie, return None.
    """

    def sieve(n):
        # Sieve of Eratosthenes algorithm to find all prime numbers up to n
        is_prime = [True] * (n + 1)
        p = 2
        while (p * p <= n):
            if is_prime[p]:
                for i in range(p * p, n + 1, p):
                    is_prime[i] = False
            p += 1
        prime_counts = [0] * (n + 1)
        count = 0
        for p in range(2, n + 1):
            if is_prime[p]:
                count += 1
            prime_counts[p] = count
        return prime_counts

    max_num = max(nums)
    prime_counts = sieve(max_num)

    maria_wins = 0
    ben_wins = 0

    for n in nums:
        if prime_counts[n] % 2 == 0:
            ben_wins += 1
        else:
            maria_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
