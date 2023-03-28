#!/usr/bin/python3
"""
Solution to lockboxes problem
"""


def canUnlockAll(boxes):
    keys = [0]  # list of keys available to the player
    unlocked = [False] * len(boxes)  # list of boxes unlocked by the player
    unlocked[0] = True  # player starts with box 0 unlocked
    
    while keys:
        box_idx = keys.pop()
        for key in boxes[box_idx]:
            if key >= 0 and key < len(boxes) and not unlocked[key]:
                keys.append(key)
                unlocked[key] = True
    
    return all(unlocked)

boxes = [[1], [2], [3], [4], []]
print(canUnlockAll(boxes))  # True

boxes = [[1, 4, 6], [2], [0, 4, 1], [5, 6, 2], [3], [4, 1], [6]]
print(canUnlockAll(boxes))  # True

boxes = [[1, 4], [2], [0, 4, 1], [3], [], [4, 1], [5, 6]]
print(canUnlockAll(boxes))  # False
