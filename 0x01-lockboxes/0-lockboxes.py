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
