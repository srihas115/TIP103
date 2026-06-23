# Problem 4: Pilot Training

You are applying to become a pilot for CodePath Airlines, and you must complete a series of flight training courses. There are a total of `num_courses` flight courses you have to take, labeled from `0` to `num_courses - 1`. Some courses have prerequisites that must be completed before you can take the next one.

You are given an array `flight_prerequisites` where `flight_prerequisites[i] = [a, b]` indicates that you must complete course `b` first in order to take course `a`.

For example, the pair `["Advanced Maneuvers", "Basic Navigation"]` indicates that to take `"Advanced Maneuvers"`, you must first complete `"Basic Navigation"`.

Return `True` if it is possible to complete all flight training courses. Otherwise, return `False`.

```python
def can_complete_flight_training(num_courses, flight_prerequisites):
    pass
```

Example Usage:

```python
flight_prerequisites_1 = [['Advanced Maneuvers', 'Basic Navigation']]
flight_prerequisites_2 = [['Advanced Maneuvers', 'Basic Navigation'], ['Basic Navigation', 'Advanced Maneuvers']]

print(can_complete_flight_training(2, flight_prerequisites_1))
print(can_complete_flight_training(2, flight_prerequisites_2))
```

Example Output:

```markdown
True
Example 1 Explanation: There are 2 flight training courses. To take *Advanced Maneuvers*, you must first complete *Basic Navigation*. This is possible.
False
Example 1 Explanation: There are 2 flight training courses. To take *Advanced Maneuvers*, you must first complete *Basic Navigation*, but to take *Basic Navigation*, you must first complete *Advanced Maneuvers*. This creates a cycle, making it impossible to complete all courses.
```

<details>
  <summary><strong>💡 Hint: BFS or DFS?</strong></summary>

This problem requires you to use either BFS or DFS. But which should you choose? Check out the *BFS vs DFS* section of the unit cheatsheet or conduct your own research to determine which algorithm would best suit this problem.

</details>
