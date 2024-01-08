# 0x01-lockboxes

This directory contains a Python script, `0-lockboxes.py`, that defines a function to determine if all the boxes in a list can be unlocked, starting from the first box (index 0).

## Function: `canUnlockAll`

### Description

The `canUnlockAll` function takes a list of boxes as input, where each element is a list representing a box. The ith box (0-based index) contains keys to other boxes specified by the indices in the list. The function determines whether all the boxes can be unlocked, starting from the first box (index 0).

### Signature

```python
def canUnlockAll(boxes):
    """
    Determines if all the boxes in a list can be unlocked, starting from the first box (index 0).

    Parameters:
    - boxes (list of lists): A list where each element is a list representing a box. The ith box (0-based index)
                             contains keys to other boxes specified by the indices in the list.

    Returns:
    - bool: True if all boxes can be unlocked, False otherwise.
    ```

### Usage

```python
from lockboxes import canUnlockAll

# Example usage
boxes = [[1], [2], [3], [4], []]
print(canUnlockAll(boxes))  # Output: True

boxes = [[1, 4, 6], [2], [0, 4, 1], [5, 6, 2], [3], [4, 1], [6]]
print(canUnlockAll(boxes))  # Output: True

boxes = [[1, 4], [2], [0, 4, 1], [3], [], [4, 1], [5, 6]]
print(canUnlockAll(boxes))  # Output: False
```

### Additional Usage

The functionality of canUnlockAll can also be demonstrated using 
a separate Python script, for example, main_0.py:

```
$ cat main_0.py

#!/usr/bin/python3

canUnlockAll = __import__('0-lockboxes').canUnlockAll

boxes = [[1], [2], [3], [4], []]
print(canUnlockAll(boxes))

boxes = [[1, 4, 6], [2], [0, 4, 1], [5, 6, 2], [3], [4, 1], [6]]
print(canUnlockAll(boxes))

boxes = [[1, 4], [2], [0, 4, 1], [3], [], [4, 1], [5, 6]]
print(canUnlockAll(boxes))
```


When executed, the above script (main_0.py) produces the following output:

```
$ ./main_0.py
True
True
False
```
