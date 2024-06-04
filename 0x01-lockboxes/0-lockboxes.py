#!/usr/bin/python3
"""
This script is a method that determines if all the boxes can be opened

"""


def canUnlockAll(boxes):
    n = len(boxes)
    opened = [False] * n
    opened[0] = True

    queue = [0]
    while queue:
        current = queue.pop(0)
        for key in boxes[current]:
            if key < n and not opened[key]:
                opened[key] = True

                queue.append(key)

    return all(opened)
