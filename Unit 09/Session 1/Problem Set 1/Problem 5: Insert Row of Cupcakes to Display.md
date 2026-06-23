# Problem 5: Insert Row of Cupcakes to Display

You have a cupcake display represented by a binary tree where each node represents a different cupcake in the display and each node value represents the flavor of the cupcake. Given the root of the binary tree `display` a string `flavor` and an integer `depth`, insert a row of nodes with value `flavor` at the given depth `depth`.

Note that the root node has depth `1`.

The inserting rule is: 

- Given the integer `depth`, for each existing tree node `cur` at the depth `depth - 1`, create two cupcakes with value `flavor` as `cur`'s left subtree root and right subtree root.
- `cur`'s original left subtree should be the left subtree of the new left subtree root.
- `cur`'s original right subtree should be the right subtree of the new right subtree root.
- If `depth == 1` that means there is no depth `depth - 1` at all, then create a cupcake with value `flavor` as the new root of the whole original tree, and the original tree is the new root's left subtree.

Evaluate the time and space complexity of your function. Define your variables and provide a rationale for why you believe your solution has the stated time and space complexity. Assume the input tree is balanced when calculating time complexity.

```python
class TreeNode():
    def __init__(self, sweetness, left=None, right=None):
        self.val = sweetness
        self.left = left
        self.right = right

def insert_row(display, flavor, depth):
    pass
```

```python
"""
        Chocolate
        /        \
    Vanilla    Strawberry
                /     \
         Chocolate    Red Velvet
"""
# Using build_tree() function included at top of page
cupcake_flavors = ["Chocolate", "Vanilla", "Strawberry", None, None, "Chocolate", "Red Velvet"]
display = build_tree(cupcake_flavors)

# Using print_tree() function included at top of page
print_tree(insert_row(display, "Mocha", 3))
```

Example Output:

```plaintext
['Chocolate', 'Vanilla', 'Strawberry', 'Mocha', 'Mocha', 'Mocha', 'Mocha', None, None, None, None, 'Chocolate', None, None, 'Red Velvet']
Explanation:
Tree with inserted row:
                   Chocolate
                   /        \
             Vanilla        Strawberry
             /    \         /       \
          Mocha   Mocha  Mocha     Mocha
                         /             \
                      Chocolate       Red Velvet
```
