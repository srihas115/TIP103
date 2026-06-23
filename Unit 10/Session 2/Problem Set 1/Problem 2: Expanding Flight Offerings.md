# Problem 2: Expanding Flight Offerings

CodePath Airlines wants to expand their flight offerings so that for any airport they operate out of, it is possible to reach all other airports. They track their current flight offerings in an adjacency dictionary `flights` where each key is an airport `i` and `flights[i]` is an array indicating that there is a flight from destination `i` to each destination in `flights[i]`. Assume that if there is flight from airport `i` to airport `j`, the reverse is also true. 

Given `flights`, return the minimum number of flights (edges) that need to be added such that there is flight path from each airport in `flights` to every other airport. 

```python
def min_flights_to_expand(flights):
    pass
```

Example Usage: 

```python
flights = {
    'JFK': ['LAX', 'SFO'],
    'LAX': ['JFK', 'SFO'],
    'SFO': ['JFK', 'LAX'],
    'ORD': ['ATL'],
    'ATL': ['ORD']
}

print(min_flights_to_expand(flights))
```

Example Output: 

```markdown
1
```
