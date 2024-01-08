#!/usr/bin/python3
"""A module for lockboxes """


def canUnlockAll(boxes):
    """
    Determines if all the boxes in a list can be unlocked, starting from the
    first box (index 0).

    Parameters:
    - boxes (list of lists): A list where each element is a list representing
                            a box.
                            The ith box (0-based index) contains keys to other
                            boxes specified by the indices in the list.

    Returns:
    - bool: True if all boxes can be unlocked, False otherwise
   """
    n = len(boxes)
    seen_boxes = set([0])
    unseen_boxes = set(boxes[0]).difference(set([0]))
    while len(unseen_boxes) > 0:
        boxIdx = unseen_boxes.pop()
        if not boxIdx or boxIdx >= n or boxIdx < 0:
            continue
        if boxIdx not in seen_boxes:
            unseen_boxes = unseen_boxes.union(boxes[boxIdx])
            seen_boxes.add(boxIdx)
    return n == len(seen_boxes)
