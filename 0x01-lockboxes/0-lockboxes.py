#!/usr/bin/python3
"""LockBoxes Challeng"""

from collections import deque


def canUnlockAll(boxes):
    # Initialize the queue and the set of unlocked boxes
    queue = deque([0])
    unlocked = set([0])
    # Process the queue
    while queue:
        current_box = queue.popleft()
        # Access the keys in the current box
        for key in boxes[current_box]:
            # If the key corresponds to an unopened box, unlock it
            if key not in unlocked and key < len(boxes):
                unlocked.add(key)
                queue.append(key)
    # Check if all boxes are unlocked
    return len(unlocked) == len(boxes)
