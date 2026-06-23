# Problem 3: Celebrity Rivalry Loops

In Hollywood, celebrity rivalries can escalate quickly. Sometimes, a rivalry between two stars leads to a chain reaction of other stars getting involved. You're tasked with determining if any group of celebrities is involved in a rivalry loop, where a rivalry escalates back to its origin.

You are given an adjacency list `rivalries`, where `rivalries[i]` represents the celebrities that celebrity `i` has a rivalry with. Write a function that detects whether any rivalry loops exist. A rivalry loop exists if there is a cycle of rivalries, where one celebrity's feud eventually leads back to themselves through others.

```python
def has_rivalry_loop(rivalries):
    pass
```

Example Usage:

```python
rivalries_1 = [
    [1],
    [0, 2],
    [1, 3],
    [2]
]

rivalries_2 = [
    [1],
    [2],
    [3],
    [0]
]

print(has_rivalry_loop(rivalries_1))  
print(has_rivalry_loop(rivalries_2)) 
```

Example Output:

```markdown
False
True
```

<details>
  <summary><strong>💡 Hint: BFS or DFS?</strong></summary>

This problem requires you to use either BFS or DFS. But which should you choose? Check out the *BFS vs DFS* section of the unit cheatsheet or conduct your own research to determine which algorithm would best suit this problem.

</details>
