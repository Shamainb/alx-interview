#!/usr/bin/python3

def isWinner(x, nums):
    if not nums or x < 1:
        return None
    
    max_num = max(nums)
    
    # Generate a prime sieve for numbers up to max_num using Sieve of Eratosthenes
    primes = [True] * (max_num + 1)
    primes[0] = primes[1] = False  # 0 and 1 are not primes
    for i in range(2, int(max_num**0.5) + 1):
        if primes[i]:
            for j in range(i * i, max_num + 1, i):
                primes[j] = False
    
    # Precompute the number of primes up to each number i
    prime_count_up_to = [0] * (max_num + 1)
    for i in range(1, max_num + 1):
        prime_count_up_to[i] = prime_count_up_to[i - 1] + (1 if primes[i] else 0)
    
    # Maria's and Ben's win count
    maria_wins = 0
    ben_wins = 0
    
    # Simulate each game
    for n in nums:
        if prime_count_up_to[n] % 2 == 0:
            ben_wins += 1  # Ben wins if the number of primes is even
        else:
            maria_wins += 1  # Maria wins if the number of primes is odd
    
    # Determine the overall winner
    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
