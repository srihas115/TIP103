# Problem 4: Convert Binary Tree of Bakery Orders to Linked List

You've been storing your bakery's orders in a binary tree where each node represents an order for a while now, but are wondering whether a new system would work better for you. You want to try storing orders in a linked list instead.

Given the root of a binary tree `orders`, flatten the tree into a 'linked list'. 
- The 'linked list' should use the same `TreeNode` class where the `right` child points to the next node in the list and the `left` child pointer is always `None`. 
- The 'linked list' should be in the same order as a preorder traversal of the binary tree.

Evaluate the time and space complexity of your function. Define your variables and provide a rationale for why you believe your solution has the stated time and space complexity. Evaluate the complexities for both a balanced and unbalanced tree.

```python
class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right

def flatten_orders(orders):
    pass
```

Example Usage:

```python
"""
        Croissant
       /         \
    Cupcake      Bagel
   /      \           \
Cake     Pie         Blondies
"""
# Using build_tree() function included at the top of page
items = ["Croissant", "Cupcake", "Bagel", "Cake", "Pie", None, "Blondies"]
orders = build_tree(items)

# Using print_tree() function included at the top of page
print_tree(flatten_orders(orders))
```

Example Output:

```plaintext
['Croissant', None, 'Cupcake', None, 'Cake', None, 'Pie', None, 'Bagel', None, 'Blondies']
Explanation:
'Linked List':
Croissant
    \
   Cupcake
       \
       Cake
         \
         Pie
           \
           Bagel
             \
            Blondies
```
