# Problem 8: Number of Airline Regions

CodePath Airlines operates in different regions around the world. Some airports are connected directly with flights, while others are not. However, if airport `a` is connected directly to airport `b`, and airport `b` is connected directly to airport `c`, then airport `a` is indirectly connected to airport `c`.

An airline region is a group of directly or indirectly connected airports and no other airports outside of the group.

You are given an `n x n` matrix `is_connected` where `is_connected[i][j] = 1` if CodePath Airlines offers a direct flight between airport `i` and airport `j`, and `is_connected[i][j] = 0` otherwise.

Return the total number of airline regions operated by CodePath Airlines.

```python
def num_airline_regions(is_connected):
    pass
```

Example Usage:

```python
is_connected1 = [
    [1, 1, 0],
    [1, 1, 0],
    [0, 0, 1]
]

is_connected2 = [
    [1, 0, 0, 1],
    [0, 1, 1, 0],
    [0, 1, 1, 0],
    [1, 0, 0, 1]
]

print(num_airline_regions(is_connected1))
print(num_airline_regions(is_connected2)) 
```

Example Output:

```markdown
2
2
```

<br>
