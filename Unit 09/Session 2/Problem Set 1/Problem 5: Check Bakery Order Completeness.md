# Problem 5: Check Bakery Order Completeness

You have a customer order you are currently making stored in a binary tree where each node represents a different item in the order. Given the `root` of the order you are fulfilling, return `True` if the order is complete and `False` otherwise.

An order is complete if every level of the tree, except possibly the last, is completely filled with items (nodes), and all items in the last level are as far left as possible. It can have between `1` and `2^h` items inclusive at the last level `h` where levels are 0-indexed. 

Evaluate the time and space complexity of your function. Define your variables and provide a rationale for why you believe your solution has the stated time and space complexity. Evaluate the complexities for both a balanced and unbalanced tree.

```python
class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right

def is_complete(root):
    pass
```

Example Usage:

```python
"""
        Croissant
       /         \
    Cupcake      Bagel
   /      \      /
Cake     Pie  Blondies
"""
# Using build_tree() function included at the top of page
items = ["Croissant", "Cupcake", "Bagel", "Cake", "Pie", "Blondies"]
order1 = build_tree(items)

"""
        Croissant
       /         \
    Cupcake      Bagel
   /      \           \
Cake     Pie         Blondies
"""
items = ["Croissant", "Cupcake", "Bagel", "Cake", "Pie", None, "Blondies"]
order2 = build_tree(items)

print(is_complete(order1))
print(is_complete(order2))
```

Example Output:

```markdown
True
False
```
