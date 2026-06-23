# Problem 7: Number of Flights

You are a travel planner and have an adjacency matrix `flights` with `n` airports labeled `0` to `n-1` where `flights[i][j]` indicates CodePath Airlines offers a flight from airport `i` to airport `j`. You are planning a trip for a client and want to know the minimum number of flights (edges) it will take to travel from airport `start` to their final destination airport `destination` on CodePath Airlines. 

Return the minimum number of flights needed to travel from airport `i` to airport `j`. If it is not possible to fly from airport `i` to airport `j`, return `-1`. 

```python
def counting_flights(flights, i, j):
    pass
```

Example Usage:

```python

# Example usage
flights = [
    [0, 1, 1, 0, 0], # Airport 0
    [0, 0, 1, 0, 0], # Airport 1
    [0, 0, 0, 1, 0], # Airport 2
    [0, 0, 0, 0, 1], # Airport 3
    [0, 0, 0, 0, 0]  # Airport 4
]

print(counting_flights(flights, 0, 2))  
print(counting_flights(flights, 0, 4))
print(counting_flights(flights, 4, 0))
```

Example Output:

```markdown
1 
Example 1 Explanation: Flight path: 0 -> 2
3
Example 2 Explanation: Flight path 0 -> 2 -> 3 -> 4
-1
Explanation: Cannot fly from Airport 4 to Airport 0
```

<details>
  <summary><strong>💡 Hint: BFS or DFS?</strong></summary>

This problem requires you to use either BFS or DFS. But which should you choose? Check out the *BFS vs DFS* section of the unit cheatsheet or conduct your own research to determine which algorithm would best suit this problem.

</details>
