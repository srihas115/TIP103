# Problem 2: Reverse Odd Levels of the Hotel

A poltergeist has been causing mischief and reversed the order of rooms on odd level floors. Given the root of a binary tree `hotel` where each node represents a room in the hotel and the root, restore order by reversing the node values at each odd level in the tree.

For example, suppose the rooms on level 3 have values `[308, 307, 306, 305, 304, 303, 302, 301]`. It should become `[301, 302, 303, 304, 305, 306, 307, 308]`.

Return the root of the altered tree. 

A binary tree is perfect if all parent nodes have two children and all leaves are on the same level.

The level of a node is the number of edges along the path between it and the root node.

Evaluate the time complexity of your function. Define your variables and provide a rationale for why you believe your solution has the stated time complexity. Assume the input tree is balanced when calculating time complexity. 

```python
class TreeNode():
     def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right

def reverse_odd_levels(hotel):
    pass
```

Example Usage:

```python
"""
        Lobby
      /      \
     102     101
     / \     /  \
   201 202 203 204 
"""
hotel = Room("Lobby", 
            Room(102, Room(201), Room (202)), 
                Room(101, Room(203), Room(204)))

# Using print_tree() function included at the top
print_tree(reverse_odd_levels(hotel))
```

Example Output:

```plaintext
['Lobby', 101, 102, 201, 202, 203, 204]

Explanation:
Updated Tree Structure:
        Lobby
      /      \
     101     102
     / \     /  \
   201 202 203 204 
```

<details>
  <summary><strong>💡 Hint: Choosing your Traversal Method</strong></summary>

This problem can be solved multiple ways, but may work best with a modified breadth first search traversal. To learn more about how to choose a traversal algorithm visit the How to Pick a Traversal Algorithm section of the unit cheatsheet.

</details>
