# Problem 6: Reinforce the Kingdom's Strongholds

In the kingdom, there are `n` strongholds positioned at various integer coordinates on a 2D map. Each stronghold is represented as a stone located at <code>[x<sub>i</sub>, y<sub>i</sub>]</code> on the map. No two strongholds occupy the same location.

To optimize the kingdom’s defenses, you can remove a stronghold if it shares the same row or column as another stronghold that hasn’t been removed yet. Your goal is to remove as many strongholds as possible while maintaining the defensive structure.

Given an array `strongholds` of length `n`, where <code>strongholds[i] = [x<sub>i</sub>, y<sub>i</sub>]</code> represents the location of the `i`-th stronghold, return the largest possible number of strongholds that can be removed.

```python
def reinforce_strongholds(strongholds):
    pass
```

Example Usage:

```python
strongholds_1 = [[0,0], [0,1], [1,0], [1,2], [2,1], [2,2]]
strongholds_2 = [[0,0], [0,2], [1,1], [2,0], [2,2]]
strongholds_3 = [[0,0]]

print(reinforce_strongholds(strongholds_1))
print(reinforce_strongholds(strongholds_2))
print(reinforce_strongholds(strongholds_3))
```

Example Output:

```markdown
5
Example 1 Explanation: One way to remove 5 strongholds is as follows:
1. Remove stronghold [2,2] because it shares the same row as [2,1].
2. Remove stronghold [2,1] because it shares the same column as [0,1].
3. Remove stronghold [1,2] because it shares the same row as [1,0].
4. Remove stronghold [1,0] because it shares the same column as [0,0].
5. Remove stronghold [0,1] because it shares the same row as [0,0].
Stronghold [0,0] cannot be removed since it no longer shares a row/column with any other stronghold still on the map.

3
Example 2 Explanation: One way to remove 3 strongholds is as follows:
1. Remove stronghold [2,2] because it shares the same row as [2,0].
2. Remove stronghold [2,0] because it shares the same column as [0,0].
3. Remove stronghold [0,2] because it shares the same row as [0,0].
Strongholds [0,0] and [1,1] cannot be removed since they no longer share a row/column with any other stronghold still on the map.

0
Example 3 Explanation: Stronghold [0,0] is the only stronghold on the map, so you cannot remove it.
```

<details>
  <summary><strong>✨ AI Hint: Union Find/Disjoint Set Union</strong></summary>

*Key Skill: Use AI to explain code concepts*

This problem can be solved using Union Find, also called Disjoint Set Union. Learn more quickly by referencing the [Unit 11 Cheatsheet](https://courses.codepath.org/courses/tip103/unit/11#!cheatsheet)

To explore further, try asking an AI tool like ChatGPT or GitHub Copilot to explain the concept of Union Find, along with examples of how it works.

</details>
