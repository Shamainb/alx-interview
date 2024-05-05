#!/usr/bin/python3
def can_unlock_all(boxes):
    visited = set()
    all_boxes_opened = True

    # Start with the first box
    visited.add(0)
    queue = [0]

    # Breadth-First Search traversal
    while queue:
        box_num = queue.pop(0)

        for key in boxes[box_num]:
            if key not in visited:
                visited.add(key)
                if key < len(boxes):
                    queue.append(key)
                else:
                    all_boxes_opened = False

    # Check if all boxes can be opened
    return len(visited) == len(boxes) and all_boxes_opened
