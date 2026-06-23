# Problem 5: Find Itinerary

You are a traveler about to embark on a multi-leg journey with multiple flights to arrive at your final travel destination. You have all your boarding passes, but their order has gotten all messed up! You want to organize your boarding passes in the order you will use them, from your first flight all the way to your last flight that will bring you to your final destination.

Given a list of edges `boarding_passes` where each element `boarding_passes[i] = (departure_airport, arrival_airport)` represents a flight from `departure_airport` to `arrival_airport`, return an array with the itinerary listing out the airports you will pass through in the order you will visit them. Assume that departure is scheduled from every airport except the final destination, and each airport is visited only once (i.e., there are no cycles in the route). 

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

One possible approach to this problem is to use a dictionary.

1.  Create a dictionary that maps each deaprture airport to its corresponding arrival airport for efficient lookup.

2.  Identify the starting airport. It is the only airport that is only a departure airport and never an arrival airport.

3.  Trace the itinerary by following the mapping from departure to arrival until there are no more flights.

</details>
