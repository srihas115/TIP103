# Problem 3: Most Popular Cookie Combo

In your bakery, each cookie order is represented by a binary tree where each node contains the number of cookies of a particular type. The cookie combo for any node is defined as the total number of cookies in the entire subtree rooted at that node (including that node itself).

Given the `root` of a cookie order tree, return an array of the most frequent cookie combo in your bakery's orders. If there is a tie, return all the most frequent combos in any order.

Evaluate the time and space complexity of your function. Define your variables and provide a rationale for why you believe your solution has the stated time and space complexity. Evaluate the complexities for both a balanced and unbalanced tree.

```python
class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right

def most_popular_cookie_combo(root):
    pass
```

Example Usage:

```python
"""
       5
      / \
     2  -3
"""
cookies1 = TreeNode(5, TreeNode(2), TreeNode(-3))

"""
       5
      / \
     2  -5
"""
cookies2 = TreeNode(5, TreeNode(2), TreeNode(-5))

print(most_popular_cookie_combo(cookies1))  
print(most_popular_cookie_combo(cookies2))  
```

Example Output:

```markdown
[2, 4, -3]
[2]
```
