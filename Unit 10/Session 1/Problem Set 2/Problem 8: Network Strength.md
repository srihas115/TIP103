# Problem 8: Network Strength

Given a group of celebrities as an adjacency dictionary `celebrities`, return `True` if the group is strongly connected and `False` otherwise. The list `celebrities[i]` is the list of all celebrities celebrity `i` likes. Mutual like between two celebrities is not guaranteed. The graph is said to be strongly connected if every celebrity likes every other celebrity in the network. 

```python
def is_strongly_connected(celebrities):
    pass
```

Example Usage:

```python
celebrities1 = {
    "Dev Patel": ["Meryl Streep", "Viola Davis"],
    "Meryl Streep": ["Dev Patel", "Viola Davis"],
    "Viola Davis": ["Meryl Streep", "Dev Patel"]
}

celebrities2 = {
    "John Cho": ["Rami Malek", "Zoe Saldana", "Meryl Streep"],
    "Rami Malek": ["John Cho", "Zoe Saldana", "Meryl Streep"],
    "Zoe Saldana": ["Rami Malek", "John Cho", "Meryl Streep"],
    "Meryl Streep": []
}

print(is_strongly_connected(celebrities1))
print(is_strongly_connected(celebrities2))
```

Example Output: 

```markdown
True
False
```

<br>
