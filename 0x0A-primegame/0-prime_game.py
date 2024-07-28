#!/usr/bin/python3
'''Prime Game'''


def isWinner(x, nums):
    '''Determines the winner after x rounds'''
    if x < 1 or not nums:
        return None

    # Counter for the wins
    winnerCounter = {'Maria': 0, 'Ben': 0}

    for n in nums:
        # Find the round winner
        roundWinner = isRoundWinner(n)
        if roundWinner:
            winnerCounter[roundWinner] += 1

    if winnerCounter['Maria'] > winnerCounter['Ben']:
        return 'Maria'
    elif winnerCounter['Ben'] > winnerCounter['Maria']:
        return 'Ben'
    else:
        return None


def isRoundWinner(n):
    '''Determines the winner of a single round'''
    if n < 1:
        return None

    # List of numbers from 1 to n
    numbers = list(range(1, n + 1))
    players = ['Maria', 'Ben']
    currentPlayerIndex = 0

    while True:
        currentPlayer = players[currentPlayerIndex]
        madeMove = False

        for num in numbers:
            if isPrime(num):
                # Remove the prime number and its multiples
                numbers = [x for x in numbers if x % num != 0]
                madeMove = True
                break

        if not madeMove:
            # No move can be made, current player loses
            return players[1 - currentPlayerIndex]

        # Switch to the other player
        currentPlayerIndex = 1 - currentPlayerIndex


def isPrime(num):
    '''Check if a number is prime'''
    if num <= 1:
        return False
    if num <= 3:
        return True
    if num % 2 == 0 or num % 3 == 0:
        return False
    i = 5
    while i * i <= num:
        if num % i == 0 or num % (i + 2) == 0:
            return False
        i += 6
    return True
