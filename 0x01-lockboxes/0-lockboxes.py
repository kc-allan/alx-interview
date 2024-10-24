#!/usr/bin/python3
"""
- You have n number of locked boxes in front of you.\
    Each box is numbered sequentially from 0 to n-1 and each box may contain keys to other boxes.
- Write a method that determines if all the boxes can be opened.\
    Prototype: def canUnlockAll(boxes)\
    boxes: is a list of lists.
A key with the same number as a box opens that box
You can assume all keys will be positive integers
- There can be keys that do not have boxes.
The first box boxes[0] is unlocked
Return -> True if all boxes can be opened else return false
A box can be - open, closed, checked or unchecked000000
"""
def canUnlockAll(boxes):
    n = len(boxes)
    if n == 0:
        return False
    unlocked = {0}
    keys = set(boxes[0])
    while keys:
        new_key = keys.pop()
        if new_key < n and new_key not in unlocked:
            unlocked.add(new_key)
            keys.update(k for k in boxes[new_key] if k < n and k not in unlocked)
    return len(unlocked) == n