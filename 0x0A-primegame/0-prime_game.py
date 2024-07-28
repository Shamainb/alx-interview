#!/usr/bin/python3
'''Prime Game'''


def isWinner(x, nums):
    '''finds the winner'''
    winnerCounter = {'Maria': 0, 'Ben': 0}

    for i in range(x):
        roundWinner = isRoundWinner(nums[i])
        if roundWinner is not None:
            winnerCounter[roundWinner] += 1

    if winnerCounter['Maria'] > winnerCounter['Ben']:
        return 'Maria'
    elif winnerCounter['Ben'] > winnerCounter['Maria']:
        return 'Ben'
    else:
        return None


def isRoundWinner(n):
    '''find round winner'''
    list = [i for i in range(1, n + 1)]
    players = ['Maria', 'Ben']
    currentPlayerIndex = 0

    while True:
        currentPlayer = players[currentPlayerIndex]
        madeMove = False
        for num in list:
            if isPrime(num):
                list = [x for x in list if x % num != 0]
                madeMove = True
                break

        if not madeMove:
            return players[1 - currentPlayerIndex]

        currentPlayerIndex = 1 - currentPlayerIndex


def isPrime(n):
    '''check if number is prime'''
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True
