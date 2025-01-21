#!/usr/bin/python3
"""
 Prime Game module
"""


def isWinner(x, nums):
    """
    Function that returns the name of the player that won the most rounds
    :param x: number of rounds
    :param nums: list of integers
    :return: name of the player that won the most rounds
    """
    count_wins = {
        "Maria": 0,
        "Ben": 0
    }
    for nm in nums:
        primes = [True for i in range(nm + 1)]  # True if nm is prime
        current = 2  # First prime number
        maria_wins = False
        while current <= nm:  # Sieve of Eratosthenes
            if primes[current] == True:  # If current is prime
                maria_wins = not maria_wins  # Change player
                # Mark all multiples of current as False
                for i in range(current * current, nm + 1, current):
                    primes[i] = False

            current += 1  # Next number
        # Add win to player
        count_wins["Maria"] + 1 if maria_wins else count_wins["Ben"] + 1
        # Return player with most wins
        return "Maria" if count_wins["Maria"] > count_wins["Ben"] else "Ben"
