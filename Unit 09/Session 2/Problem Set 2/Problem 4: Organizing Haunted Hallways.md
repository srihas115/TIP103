# Problem 4: Organizing Haunted Hallways

The haunted hotel is expanding, and the management wants to add new hallways filled with rooms that must be carefully arranged to maintain a spooky atmosphere. Given an integer array `rooms` sorted in ascending order where each element represents a unique room number, write a function that converts the array into a height-balanced binary search tree (BST) and returns the root of the balanced tree. 

Evaluate the time and space complexity of your function. Define your variables and provide a rationale for why you believe your solution has the stated time and space complexity. Evaluate the complexities for both a balanced and unbalanced tree.

```python
class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right

def array_to_bst(rooms):
    pass
```

Example Usage:

```python
rooms = [4, 7, 13, 666, 1313]

# Using print_tree() function included at top of page
print_tree(array_to_bst(rooms))
```

Example Output:

```markdown
[13, 7, 1313, 4, None, 666]
Explanation:
Balanced Tree:
       13
      /  \
    7    1313 
  /       / 
 4       666

[13, 4, 666, None, 7, 1313] is also an acceptable answer.

        13
      /  \
     4   666 
      \     \   
       7    1313
```
