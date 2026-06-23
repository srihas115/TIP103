# Problem 4: Celebrity Feuds

You are in charge of scheduling celebrity arrival times for a red carpet event. To make things easy, you want to split the group of `n` celebrities labeled from `1` to `n` into two different arrival groups. 

However, your boss has just informed you that some celebrities don't get along, and celebrities who dislike each other may not be in the same arrival group. Given the number of celebrities who will be attending `n`, and an array `dislikes` where `dislikes[i] = [a, b]` indicates that the person labeled `a` does not get along with the person labeled `b`, return `True` if it is possible to split the celebrities into two arrival periods and `False` otherwise.

```python
def can_split(n, dislikes):
    pass
```

Example Usage:

```python
dislikes_1 = [[1, 2], [1, 3], [2, 4]]
dislikes_2 = [[1, 2], [1, 3], [2, 3]]

print(can_split(4, dislikes_1))
print(can_split(3, dislikes_2))
```

Example Output:

```markdown
True
False
```

<details>
  <summary><strong>💡 Hint: Bipartite Graphs</strong></summary>

This problem requires you to determine whether a graph is bipartite. A bipartite graph is a graph where the nodes can e divided into two distinct sets such that no two vertices in the saem set are connected by an edge. All edges must go between vertices in different sets.

We can determine whether a graph is bipartite using a technique called *graph coloring*. To determine if a graph is bipartite, we try coloring the graph using two colors: start from any node, color it one color, and color all its neighbors the opposite color. If at any point two adjacent nodes have the same color, the graph is not bipartite. You can do this using either BFS or DFS.

</details>
