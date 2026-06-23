# Problem 6: Finding Itinerary II

If you implemented `find_itinerary()` in the previous problem without using Depth First Search, solve it using DFS. If you solved it using DFS, try solving it using an alternative approach.

```python
def find_itinerary(boarding_passes):
    pass
```

Example Usage:

```python
boarding_passes_1 = [
                    ("JFK", "ATL"),
                    ("SFO", "JFK"),
                    ("ATL", "ORD"),
                    ("LAX", "SFO")]

boarding_passes_2 = [
                    ("LAX", "DXB"),
                    ("DFW", "JFK"),
                    ("LHR", "DFW"),
                    ("JFK", "LAX")]

print(find_itinerary(boarding_passes_1))
print(find_itinerary(boarding_passes_2))
```

Example Output:

```markdown
['LAX', 'SFO', 'JFK', 'ATL', 'ORD']
['LHR', 'DFW', 'JFK', 'LAX', 'DXB']
```

<details>
  <summary><strong>💡 Hint: Pseudocode</strong></summary>

One possible approach to this problem is to use Depth First Search. To use DFS:

1.  Create an adjacency list where each airport is a key and its corresponding value is a list of destinations (flights) from that airport.

2.  Identify the starting airport. It is the only airport that is only a departure airport and never an arrival airport.

3.  Using the starting airport as your start point, begin a DFS traversal of the adjacency list. After visiting *all* destinations for a given airport, add the airport to the itinerary.

4.  Since airports are added only after visiting all connected destinations, the resulting itinerary is in reverse order. Reverse the itinerary and return the result.

</details>
