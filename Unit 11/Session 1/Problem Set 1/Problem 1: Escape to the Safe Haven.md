# Problem 1: Escape to the Safe Haven

You've just learned of a safe haven at the bottom right corner of the city represented by an `m x n` matrix `grid`. However, the city is full of zombie-infected zones. Safe travel zones are marked on the grid as `1`s and infected zones are marked as `0`s. Given your current `position` as a tuple in the form `(row, column)`, return `True` if you can reach the safe haven traveling only through safe zones and `False` otherwise. From any zone (cell) in the `grid` you may move up, down, left, or right. 

Evaluate the time and space complexity of your solution. Define your variables and provide a rationale for why you believe your solution has the stated time and space complexity. Assume the input tree is balanced when calculating time and space complexity. 

<!-- Hint: We can transform the grid into a graph -->
<!-- Hint: Create helper function to check valid moves consider modifying to only return unvisited locations -->

```python
def can_move_safely(position, grid):
    pass
```

Example Usage:

```python
grid = [
    [1, 0, 1, 1, 0], # Row 0
    [1, 1, 1, 1, 0], # Row 1
    [0, 0, 1, 1, 0], # Row 2
    [1, 0, 1, 1, 1]  # Row 3
]

position_1 = (0, 0)
position_1 = (0, 4)
position_2 = (3, 0)

print(can_move_safely(position_1, grid))
print(can_move_safely(position_2, grid))
print(can_move_safely(position_3, grid))
```

Example Output: 

```markdown
True
Example 1 Explanation: Can follow the path (0, 0) -> (1, 0) -> (1, 1) -> (1, 2) -> 
(2, 2) -> (3, 2) -> (3, 3) -> (3, 4)

True
Example 2 Explanation: Although we start in an unsafe position, we can immediately
arrive in a safe position and from there safely travel to the bottom right corner (3, 4).

False
```

<details>
  <summary><strong>💡 Hint: Transforming Matrices into Graphs</strong></summary>

This problem and many other matrix problems can be solved using graph algorithms! To learn how to reimagine matrix problems as graph problems, check out the Matrices section of the cheatsheet.

</details>

<details>
  <summary><strong>💡 Hint: Create a Helper to Find Neighbors</strong></summary>

While not required to solve matrix problems, you may consider writing a helper function that helps you find the neighbors of a given cell in the matrix. That is, find the cells to the left, right, up, and down of the current cell. Neighboring cells should also be within the row and column bounds of the matrix and follow any other constraints defined by the problem.

</details>
