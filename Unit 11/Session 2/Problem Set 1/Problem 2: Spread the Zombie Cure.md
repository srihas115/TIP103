# Problem 2: Spread the Zombie Cure

In the aftermath of the zombie apocalypse, a cure has been developed to stop the infection, but it must be distributed across a network of survivor camps. The camps are connected by communication lines, and you need to determine how quickly the cure can reach all the camps. Each camp is represented as a node in the network, and each communication line is represented as a directed edge with a travel time.

You are given an integer `n`, representing the number of camps (nodes), and a list of travel times `times`, where `times[i] = (u, v, w)` indicates that it takes `w` time for the cure to travel from camp `u` to camp `v`. You will send the cure from a starting camp `k`.

Return the minimum time it takes for all camps to receive the cure. If it is impossible for all camps to receive the cure, return `-1`.

```python
def spread_cure(n, times, k):
    pass
```

Example Usage:

```python
times_1 = [(2, 1, 1), (2, 3, 1), (3, 4, 1)]
times_2 = [(1, 2, 1), (2, 3, 2), (1, 3, 4)]
times_3 = [(1, 2, 1)]

print(spread_cure(1, times_1, 2))
print(spread_cure(3, times_2, 1))
print(spread_cure(2, times_3, 2))
```

Example Output:

```markdown
2
Example 1 Explanation: Starting from camp 2, the cure travels to camp 1 in 1 unit 
of time, to camp 3 in 1 unit of time, and from camp 3 to camp 4 in 1 additional unit of time. 
The cure reaches all camps within 2 units of time.

3
Example 2 Explanation: Starting from camp 1, the cure can reach camp 2 in 1 unit 
of time and camp 3 via camp 2 in a total of 3 units of time (1+2). Therefore, the 
minimum time to reach all camps is 3 units.

-1
Example 3 Explanation: It is impossible for the cure to travel from camp 2 to camp 1 
since there is no direct or indirect communication line to connect the camps.
```

<details>
  <summary><strong>✨ AI Hint: Dijkstra's Algorithm</strong></summary>

*Key Skill: Use AI to explain code concepts*

This problem can be solved using Dijkstra's Algorithm, a very popular algorithm for finding the shortest path in a weighted graph.

For a refresher, check out the Advanced section of the [Unit 11 Cheatsheet](https://courses.codepath.org/courses/tip103/unit/11#!cheatsheet).

If you need help understanding Dijkstra's Algorithm, you can ask an AI tool like ChatGPT or GitHub Copilot to explain it to you, and even provide a step-by-step example of the algorithm in action.

We recommend trying to understand the **algorithm** first, and only attempt implementation once you have a solid grasp of how it works.

</details>

<details>
  <summary><strong>✨ AI Hint: Priority Queues</strong></summary>

*Key Skill: Use AI to explain code concepts*

Dijkstra's uses a priority queue instead of a normal queue. Check out the Priority Queue section of the [Unit 11 Cheatsheet](https://courses.codepath.org/courses/tip103/unit/11#!cheatsheet) for more information.

You can also ask an AI tool like ChatGPT or GitHub Copilot, like this:

*"What is the difference between a normal queue and a priority queue, and why do we need to use a priority queue in Dijkstra's algorithm?"*

</details>
