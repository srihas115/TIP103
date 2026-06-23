# Problem 2: Counting Room Clusters

Given the root of a binary tree `hotel` where each node represents a room in the hotel and each node value represents the theme of the room, return the number of **distinct clusters** in the hotel. A distinct cluster is defined as a group of connected rooms (connected by edges) where each room has the same theme (`val`). 

Evaluate the time and space complexity of your function. Define your variables and provide a rationale for why you believe your solution has the stated time and space complexity. Evaluate the complexities for both a balanced and unbalanced tree.

```python
class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right

def count_clusters(hotel):
    pass
```

Example Usage:

```python
"""
     👻
   /    \
  👻     🧛🏾
 /  \      \
👻  🧛🏾      🧛🏾
"""
# Using build_tree() function included at the top of the page
themes = ["👻", "👻", "🧛🏾", "👻", "🧛🏾", None, "🧛🏾"]
hotel = build_tree(themes)

print(count_clusters(themes))
```

Example Output:

```markdown
3
```
