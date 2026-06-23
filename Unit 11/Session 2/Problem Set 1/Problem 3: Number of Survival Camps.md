# Problem 3: Number of Survival Camps

There are a series of survival camps that have cropped up around the city since the zombie apocalypse started. Given an `m x n` 2D binary grid `city` which represents a map of `1`s (a survival camp) and `0`s (zombie controlled land), use Union Find to return the number of islands.

A survival camp is surrounded by zombie controlled land and is formed by connecting adjacent `1`s horizontally or vertically. You may assume all four edges of the grid are all surrounded by zombie controlled land. 

```python
def num_camps(city):
    pass
```

Example Usage:

```python
city_1 = [
  [1,1,1,1,0],
  [1,1,0,1,0],
  [1,1,0,0,0],
  [0,0,0,0,0]
]

city_2 = [
  [1,1,0,0,0],
  [1,1,0,0,0],
  [0,0,1,0,0],
  [0,0,0,1,1]
]

print(num_camps(city_1))
print(num_camps(city_2))
```

Example Output:

```markdown
1
3
```

<details>
  <summary><strong>✨ AI Hint: Union Find/Disjoint Set Union</strong></summary>

*Key Skill: Use AI to explain code concepts*

This problem can be solved using Union Find, also called Disjoint Set Union. Learn more quickly by referencing the [Unit 11 Cheatsheet](https://courses.codepath.org/courses/tip103/unit/11#!cheatsheet)

To explore further, try asking an AI tool like ChatGPT or GitHub Copilot to explain the concept of Union Find, along with examples of how it works.

</details>
