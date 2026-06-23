# Problem 4: Kth Spookiest Room in the Hotel

Over time, your hotel has gained a reputation for being haunted, and you now have customers coming specifically for a spooky experience. You are given the `root` of a binary search tree (BST) with `n` nodes where each node represents a room in the hotel and each node has an integer `key` representing the spookiness of the room (`1` being most spooky and `n` being least spooky) and `val` representing the room number. The tree is organized according to its keys. 

Given the `root` of a BST and an integer `k` write a function `kth_spookiest()` that returns the **value** of the `kth` spookiest room of all the rooms in the hotel.

Evaluate the time and space complexity of your function. Define your variables and provide a rationale for why you believe your solution has the stated time and space complexity. Assume the input tree is balanced when calculating time and space complexity. 

```python
class TreeNode():
     def __init__(self, key, value, left=None, right=None):
        self.key = key
        self.val = value
        self.left = left
        self.right = right

def kth_spookiest(root, k):
    pass
```

Example Usage:

```python
"""
    (3, Lobby) 
   /         \
(1, 101)   (4, 102)
     \
     (2, 201)
"""

# Using build_tree() function at the top of the page
rooms = [(3, "Lobby"), (1, 101), (4, 102), None, (2, 201)]
hotel1 = build_tree(rooms)

"""
            (5, Lobby) 
            /         \
        (3, 101)   (6, 102)
        /      \
    (2, 201)  (4, 202)
    /
(1, 301)
"""
rooms = [(5, 'Lobby'), (3, 101), (6, 102), (2, 201), (4, 202), None, None, (1, 301)]
hotel2 = build_tree(rooms)

print(kth_spookiest(hotel1, 1))
print(kth_spookiest(hotel2, 3))
```

Example Markdown:

```markdown
101
101
```
