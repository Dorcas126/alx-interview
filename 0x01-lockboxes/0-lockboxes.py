#!/usr/bin/python3
"""
Module for canUnlockAll.
"""


def canUnlockAll(boxes):
    """
    Determines if all the boxes can be opened.
    """
    n = len(boxes)
    seen = [False] * n
    seen[0] = True
    queue = [0]

    while queue:
        box = queue.pop(0)
        for key in boxes[box]:
            if key < n and not seen[key]:
                seen[key] = True
                queue.append(key)

    return all(seen)

