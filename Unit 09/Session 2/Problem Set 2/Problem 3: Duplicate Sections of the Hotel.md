# Problem 3: Duplicate Sections of the Hotel

On one of your shifts at the haunted hotel, you find that you keep stumbling upon the same rooms in different halls. It's almost as if some parts of the hotel are being duplicated...

Given the root of a binary tree `hotel` where each node represents a room in the hotel, return a list of the roots of all duplicate subtrees. For each duplicate subtree, you only need to return the root node of any **one** of them. Two trees are duplicate if they have the same structure and the same node values.

Evaluate the time and space complexity of your function. Define your variables and provide a rationale for why you believe your solution has the stated time and space complexity. Evaluate the complexities for both a balanced and unbalanced tree.

```python
class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right

def find_duplicate_subtrees(hotel):
    pass
```

Example Usage:

```python
"""
        Lobby
      /       \
    101      123
    /        /  \ 
  201      101  201
          /
         201
"""
# Using build_tree() function included at top of page
rooms = ["Lobby", 101, 123, 201, None, 101, 201, None, None, 201]
hotel = build_tree(rooms)

# Using print_tree() function included at top of page
subtree_lst = find_duplicate_subtrees(hotel)
for subtree in subtree_lst:
    print_tree(subtree)
```

Example Output:

```plaintext
[101, 201]
[201]
Explanation: 
Subtrees:
   Subtree 1   Subtree 2
     101         201
     /
   201
```
