#!/usr/bin/python3
"""
Finding the minimum number of coins need to make change
"""


def makeChange(coins, total):
    """
    Given a pile of coins of different values, determine the fewest number of coins needed to meet a given amount total.
    :param coins: a list of the values of the coins in your possession
    :param total: the total amount of money you need to make change for
    :return: the fewest number of coins needed to meet the total
    """
    if total <= 0:
        return 0
    answers = []

    n = len(coins)
    i = n - 1
    coins.sort()
    while i >= 0:
        while total >= coins[i]:
            total -= coins[i]
            answers.append(coins[i])
        i -= 1
    if total != 0:
        return -1

    return len(answers)
