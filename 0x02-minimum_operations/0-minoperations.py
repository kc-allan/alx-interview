#!/uar/bin/python3
"""
Implementation of the minimum operations task
"""


def minOperations(n):
    """
    Calculates the minimum number of operations (Copy All and Paste) needed to achieve n 'H' characterssssss.
    Args:\
        n (int): target number of 'H' characters to achieve.
    Returns:\
        int: The minimum number of operations needed, or 0 if impossible.
    """
    # return 0 if the number cannot be achieved or n is 1
    if n <= 1:
        return 0
    operations = 0
    # Start with the smallest factor of 2
    factor = 2

    # Continuously factcorize n
    while n > 1:
        # Check if the current factor divides n evenly
        while n % factor == 0:
            operations += factor
            # Divide n by the current factor
            n //= factor
        factor += 1

        # If the factor exceeds the square root of the original n, and n > 1,
        # then n is prime and we need n operations
        if factor * factor > n and n > 1:
            operations += n
            break
    return operations
