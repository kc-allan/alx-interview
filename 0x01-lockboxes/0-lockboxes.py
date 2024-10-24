#!/usr/bin/python3
"""
A method that determines if all the boxes can be opened.\
    Prototype: def canUnlockAll(boxes)\
    boxes: is a list of lists.
Return -> True if all boxes can be opened else return false
"""


def canUnlockAll(boxes):
    """
    Determines if all the boxes can be opened.
    Return -> True if all boxes can be opened else return false
    """
    n = len(boxes)
    if n == 0:
        return False
    unlocked = {0}
    keys = set(boxes[0])
    while keys:
        new_key = keys.pop()
        if new_key < n and new_key not in unlocked:
            unlocked.add(new_key)
            keys.update(k for k in boxes[new_key]
                        if k < n and k not in unlocked)
    return len(unlocked) == n
