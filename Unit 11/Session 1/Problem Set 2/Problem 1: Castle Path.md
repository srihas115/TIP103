# Problem 1: Castle Path

Your kingdom is represented by an `m x n` matrix `kingdom`. Each square in the matrix represents a different town in the kingdom. You wish to travel from a starting position `town` to the `castle`, however several towns have been overrun by bandits.

Towns that are safe to travel through are marked with `X`s and towns with dangerous bandits are marked with `O`s. 

Given your current `town` and the `castle` location as tuples in the form `(row, column)`, return a list of tuples representing the shortest path from your `town` to the `castle` without traveling through any towns with bandits. If there are multiple paths with the shortest length, you may return any path. If no such path exists, return `None`. 

From any town in the `grid` you may move to the neighboring towns up, down, left, or right. You may not move out of bounds of the `kingdom`. 

Evaluate the time and space complexity of your solution. Define your variables and provide a rationale for why you believe your solution has the stated time and space complexity. Assume the input tree is balanced when calculating time and space complexity. 

```python
def path_to_castle(kingdom, town, castle):
    pass
```

Example Usage:

```python
grid = [
    ['X', 'O', 'X', 'X', 'O'], # Row 'O'
    ['X', 'X', 'X', 'X', 'O'], # Row 1
    ['O', 'O', 'X', 'X', 'O'], # Row 2
    ['X', 'O', 'X', 'X', 'X']  # Row 3
]

castle = (3, 4)

town_1 = (0, 0)
town_2 = (0, 4)
town_3 = (3, 0)

print(path_to_castle(town_1, grid, castle))
print(path_to_castle(town_2, grid, castle))
print(path_to_castle(town_3, grid, castle))
```

Example Output: 

```markdown
[(0, 0), (1, 0), (1, 1), (1, 2), (2, 2), (3, 2), (3, 3), (3, 4)]

None

None
```

<details>
  <summary><strong>💡 Hint: Transforming Matrices into Graphs</strong></summary>

This problem and many other matrix problems can be solved using graph algorithms! To learn how to reimagine matrix problems as graph problems, check out the Matrices section of the cheatsheet.

</details>

<details>
  <summary><strong>💡 Hint: Create a Helper to Find Neighbors</strong></summary>

While not required to solve matrix problems, you may consider writing a helper function that helps you find the neighbors of a given cell in the matrix. That is, find the cells to the left, right, up, and down of the current cell. Neighboring cells should also be within the row and column bounds of the matrix and follow any other constraints defined by the problem.

</details>
