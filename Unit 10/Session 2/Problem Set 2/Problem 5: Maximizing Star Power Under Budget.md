# Problem 5: Maximizing Star Power Under Budget

You are the producer of a big Hollywood film and want to maximize the star power of the cast. Each collaboration between two celebrities has a star power value, and each celebrity demands a fee to be part of the project. You want to maximize the total star power of the cast while ensuring that the total cost of hiring these celebrities stays under a given budget.

You are given a graph where:

- Each vertex represents a celebrity.
- Each edge between two celebrities represents a collaboration, with two weights:
  1. The star power (benefit) they bring when collaborating.
  2. The cost to hire them both for the project.

The graph is given as a dictionary `collaboration_map` where each key is a celebrity and the corresponding value is a list of tuples. Each tuple contains a connected celebrity, the star power of that collaboration, and the cost of the collaboration. Given a `start` celebrity, `target` celebrity, and maximum `budget`, return the maximum star power it is possible for you film to have from `start` to `target`.

```python
def find_max_star_power(collaboration_map, start, target, budget):
    pass
```

Example Usage:

```python
collaboration_map = {
    "Leonardo DiCaprio": [("Brad Pitt", 40, 300), ("Robert De Niro", 30, 200)],
    "Brad Pitt": [("Leonardo DiCaprio", 40, 300), ("Scarlett Johansson", 20, 150)],
    "Robert De Niro": [("Leonardo DiCaprio", 30, 200), ("Chris Hemsworth", 50, 350)],
    "Scarlett Johansson": [("Brad Pitt", 20, 150), ("Chris Hemsworth", 30, 250)],
    "Chris Hemsworth": [("Robert De Niro", 50, 350), ("Scarlett Johansson", 30, 250)]
}

print(find_max_star_power(collaboration_map, "Leonardo DiCaprio", "Chris Hemsworth", 600))
```

Example Output:

```markdown
80
Explanation: The maximum star power while staying under budget is achieved on the path from Leonardo DiCaprio to Robert De Niro to Chris Hemsworth
```
