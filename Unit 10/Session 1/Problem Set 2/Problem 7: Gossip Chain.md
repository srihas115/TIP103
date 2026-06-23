# Problem 7: Gossip Chain

In Hollywood, rumors spread rapidly among celebrities through various connections. Imagine each celebrity is represented as a vertex in a directed graph, and the connections between them are directed edges indicating who spread the latest gossip to whom.

The arrival time of a rumor for a given celebrity is the moment the rumor reaches them for the first time, and the departure time is when all the celebrities they could influence have already heard the rumor, meaning they are no longer involved in spreading it.

Given a list of edges `connections` representing connections between celebrities and the number of celebrities in the the graph `n`, find the arrival and departure time of the rumor for each celebrity in a Depth First Search (DFS) starting from a given celebrity `start`.

Return a dictionary where each celebrity in `connections` is a key whose corresponding value is a tuple `(arrival_time, departure_time)` representing the arrival and departure times of the rumor for that celebrity. If a celebrity never hears the rumor their arrival and departure times should be `(-1, -1)`. 

```python
def rumor_spread_times(connections, n, start):
    pass
```

Example Usage:

```python
connections = [
    ["Amber Gill", "Greg O'Shea"],
    ["Amber Gill", "Molly-Mae Hague"],
    ["Greg O'Shea", "Molly-Mae Hague"],
    ["Greg O'Shea", "Tommy Fury"],
    ["Molly-Mae Hague", "Tommy Fury"],
    ["Tommy Fury", "Ovie Soko"],
    ["Curtis Pritchard", "Maura Higgins"]
]

print(rumor_spread_times(connections, 7, "Amber Gill"))
```

Example Output:

```markdown
{
    "Amber Gill": (1, 12),
    "Greg O'Shea": (2, 11),
    "Molly-Mae Hague": (3, 8),
    "Tommy Fury": (4, 7),
    "Ovie Soko": (5, 6),
    "Curtis Pritchard": (-1, -1),
    "Maura Higgins": (-1, -1)
}
```
