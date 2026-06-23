# Problem 2: List All Escape Routes

Having arrived at the safe haven, you are immediately put to work evaluating how many civilians can be evacuated to the safe haven. Given an `m x n` `grid` representing the city, return a list of tuples of the form `(row, column)` representing every starting position in the `grid` from which there exists a valid path of safe zones (`1`s) to the safe haven in the bottom-right corner of the grid. 

If the starting cell has value `0`, they are considered infected and cannot reach the safe haven.

```python
def list_all_escape_routes(grid):
    pass
```

Example Usage:

```python
grid = [
    [1, 0, 1, 0, 1], # Row 0
    [1, 1, 1, 1, 0], # Row 1
    [0, 0, 1, 0, 0], # Row 2
    [1, 0, 1, 1, 1]  # Row 3
]

print(list_all_escape_routes(grid))
```

Example Output:

```markdown
[(0, 0), (0, 2), (1, 0), (1, 1), (1, 2), (1, 3), (2, 2), (3, 2), (3, 3), (3, 4)]
```

<details>
  <summary><strong>💡 Hint: Repeating Traversal</strong></summary>

To solve this function, you may need to repeatedly traverse the matrix using BFS or DFS starting from all or multiple cells in the matrix.

</details>
