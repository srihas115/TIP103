# Problem 3: Get Flight Itinerary

Given an adjacency dictionary of flights `flights` where each key is an airport `i` and `flights[i]` is an array indicating that there is a flight from destination `i` to each destination in `flights[i]`, return an array with the flight path from a given `source` location to a given `destination` location. 

If there are multiple flight paths from the `source` to `destination`, return any flight path.

```python
def get_itinerary(flights, source, destination):
    pass
```

Example Usage:

```python
flights = {
    'LAX': ['SFO'],
    'SFO': ['LAX', 'ORD', 'ERW'],
    'ERW': ['SFO', 'ORD'],
    'ORD': ['ERW', 'SFO', 'MIA'],
    'MIA': ['ORD']
}

print(get_itinerary(flights, 'LAX', 'MIA'))
```

Example Output:

```markdown
['LAX', 'SFO', 'ORD', 'MIA']
Explanation: ['LAX', 'SFO', 'ERW', 'ORD', 'MIA'] is also a valid answer
```

<details>
  <summary><strong>💡 Hint: Path Reconstruction</strong></summary>

This problem requires you to reconstruct the path taken by either BFS or DFS. To reconstruct a path from BFS/DFS, we can keep track of each node's parent (the node from which it was discovered) during the search. After reaching the target, backtrack from the target node to the start using the parent pointers to trace the path.

</details>
