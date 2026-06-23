# Problem 3: Secret Celebrity

A new reality show is airing in which a famous celebrity pretends to be a non-famous person. As contestants get to know each other, they have to guess who the celebrity among them is to win the show. An even bigger twist: there might be no celebrity at all! The show has `n` contestants labeled from 1 to `n`. 

If the celebrity exists, then: 
1. The celebrity trusts none of the contestants.
2. Due to the celebrity's charisma, all the contestants trust the celebrity.
3. There is exactly one person who satisfies rules 1 and 2. 

You are given an array `trust` where `trust[i] = [a, b]` indicates that contestant `a` trusts contestant `b`. If a trust relationship does not exist in `trust` array, then such a trust relationship does not exist.

Return the label of the celebrity if they exist and can be identified. Otherwise, return `-1`.

```python
def identify_celebrity(trust, n):
    pass
```

Example Usage:

```python
trust1 = [[1,2]]
trust2 = [[1,3],[2,3]]
trust3 = [[1,3],[2,3],[3,1]]

identify_celebrity(trust1, 2)
identify_celebrity(trust2, 3)
identify_celebrity(trust3, 3)
```

Example Output:

```python
2
3
-1
```
