# Problem 5: Reinforce the Kingdom Walls

Your kingdom is represented by an `m x n` integer matrix `kingdom_grid`, where each square represents a fortified area with a particular defensive strength. The value at each square in the grid indicates the current level of fortification (color).

You are given three integers, `row`, `col`, and `new_strength`. The square at `kingdom_grid[row][col]` is part of a fortified section with a particular defensive strength, and you want to strengthen the border of this section.

The _border_ of a section is defined as all the squares in the fortified section that either:
1. Are adjacent to a square with a different defensive strength, or
2. Lie on the outer edges of the kingdom.

Your task is to identify the fortified section containing `kingdom_grid[row][col]` and reinforce the border by updating its defensive strength to `new_strength`. Return the updated `kingdom_grid` after reinforcing the border.

From any square, you may move to adjacent squares in the four cardinal directions: up, down, left, and right. Two squares are considered part of the same fortified section if they have the same defensive strength and are adjacent.

```python
def reinforce_walls(kingdom_grid, row, col, new_strength):
    pass
```

Example Input:

```python
kingdom_grid = [
    [1, 1, 1, 2],
    [1, 3, 1, 2],
    [1, 1, 1, 2]
]

print(reinforce_walls(kingdom_grid, 1, 1, 4))
```

Example Output:

```markdown
[
    [1, 1, 1, 2],
    [1, 4, 1, 2],
    [1, 1, 1, 2]
]
```
