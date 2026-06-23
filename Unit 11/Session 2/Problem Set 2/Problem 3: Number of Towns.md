# Problem 3: Number of Towns

As part of the royal survey, the kingdom is mapping out its territories. The kingdom’s lands are represented by an `m x n` 2D binary grid `map`, where:
- **1** represents **urban** land, and
- **0** represents **rural** land.

Determine how many distinct towns exist in the kingdom. An town is defined as a group of connected urban land squares, and two squares are connected if they are adjacent horizontally or vertically. Assume that the entire map is surrounded by rural land.

To solve this problem, you must use the Union Find technique to efficiently group connected urban land squares into towns.

1. Use Union Find to merge connected urban land squares.
2. Return the total number of separate towns in the map.

```python
def count_towns(grid):
    pass
```

Example Usage:

```python
kingdom_map_1 = [
    ["1", "1", "1", "1", "0"],
    ["1", "1", "0", "1", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "0", "0", "0"]
]

kingdom_map_2 = [
    ["1", "1", "0", "0", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "1", "0", "0"],
    ["0", "0", "0", "1", "1"]
]

print(count_towns(kingdom_map_1))
print(count_towns(kingdom_map_2))
```

Example Output:

```markdown
1
3
```

<details>
  <summary><strong>✨ AI Hint: Union Find/Disjoint Set Union</strong></summary>

*Key Skill: Use AI to explain code concepts*

This problem can be solved using Union Find, also called Disjoint Set Union. Learn more quickly by referencing the [Unit 11 Cheatsheet](https://courses.codepath.org/courses/tip103/unit/11#!cheatsheet)

To explore further, try asking an AI tool like ChatGPT or GitHub Copilot to explain the concept of Union Find, along with examples of how it works.

</details>
