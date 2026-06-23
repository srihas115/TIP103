# Problem 5: Lowest Common Ancestor of Youngest Children

There's a tapestry hanging up on the wall with the family tree of the cursed family who owns the hotel. Given the `root` of the binary tree where each node represents a member in the family, return the value of the lowest common ancestor of the youngest children in the family. The youngest children in the family are the deepest leaves in the tree ***at the same depth***.

Recall that:
- The node of a binary tree is a leaf if and only if it has no children
- The depth of the root of the tree is `0`. If the depth of a node is `d`, the depth of each of its children is `d + 1`.
- The lowest common ancestor of a set `S` of nodes, is the node `A` with the largest depth such that every node in `S` is in the subtree with root `A`. 

```python
class TreeNode():
     def __init__(self, key, value, left=None, right=None):
        self.key = key
        self.val = value
        self.left = left
        self.right = right

def lca_youngest_children(root):
    pass
```

Example Usage:

```python
"""
                Isadora the Hexed
                /                \
            Thorne               Raven
           /      \             /      \
      Dracula     Doom      Hecate    Wraith
                 /    \      
             Gloom   Mortis
"""
# Using build_tree() function included at top of the page
members = ["Isadora the Hexed", "Thorne", "Raven", "Dracula", "Doom", "Hecate", "Wraith", None, None, "Gloom", "Mortis"]
family1 = build_tree(members)

"""
              Grandmama Addams
              /              \
        Gomez Addams        Uncle Fester
                \
            Wednesday Addams
"""
members = ["Grandmama Addams", "Gomez Addams", "Uncle Fester", None, "Wednesday Addams"]
family2 = build_tree(members)

print(lca_youngest_children(family1))
print(lca_youngest_children(family2))
```

Example Output:

```markdown
Doom
Example 1 Explanation: Gloom and Mortis are the youngest children (deepest leaves) in the tree. 
Doom in their lowest common ancestor.

Wednesday Addams
Example 2 Explanation: The youngest child in the tree is Wednesday Addams and the lowest common ancestor
of one node is itself
```
