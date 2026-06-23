# Problem 1: Schedule Banquet Tasks

In preparation for the grand castle banquet, there are `tasks` that must be completed. Each task is represented by a string. You are given a list of dependencies called `prerequisites`, where `prerequisites[i] = [task_a, task_b]` means that you must complete `task_b` before you can complete `task_a`.

For example, if you have `prerequisites = [["prepare_dessert", "set_table"]]`, it means that you must set the table before you can prepare the dessert.

Return a list with the ordering of tasks such that all tasks can be completed in time for the banquet. If there are multiple valid orderings, return any of them. If it’s impossible to complete all the tasks (due to circular dependencies), return an empty array.

```python
def prepare_banquet(tasks, prerequisites):
    pass
```

Example Usage: 

```python
tasks_1 = ["set_table", "prepare_dessert"]
prerequisites_1 = [["prepare_dessert", "set_table"]]

tasks_2 = ["stock_pantry", "main_course", "decorations", "serve_food"]
prerequisites_2 = [["main_course", "stock_pantry"], ["decorations", "stock_pantry"], ["serve_food", "main_course"], ["serve_food", "decorations"]]

tasks_3 = ["only_task"]
prerequisites_3 = []

print(prepare_banquet(tasks_1, prerequisites_1))
print(prepare_banquet(tasks_2, prerequisites_2))
print(prepare_banquet(tasks_3, prerequisites_3))
```

Example Output:

```markdown
["set_table", "prepare_dessert"]
Example 1 Explanation: You need to set the table before you can prepare the dessert.

["stock_pantry", "main_course", "decorations", "serve_food"]  
Example 2 Explanation: 
["stock_pantry", "decorations", "main_course", "serve_food"] is also an acceptable
answer. You need to finish both cooking the main course and setting up the decorations 
before you can serve the food. Both tasks depend on stocking the pantry.

["only_task"]
Example 3 Explanation: There's only one task to complete, so you can proceed without dependencies.
```

<details>
  <summary><strong>✨ AI Hint: Topological Sort</strong></summary>

*Key Skill: Use AI to explain code concepts*

This problem may be solved with topological sort. Check out the Advanced section of the [Unit 11 Cheatsheet](https://courses.codepath.org/courses/tip103/unit/11#!cheatsheet) for more information.

If you need more info, you can ask an AI tool like ChatGPT or GitHub Copilot to help you understand topological sort. For example, you can ask:

*"What is topological sort, and when is it useful for solving coding problems?"*

*"Can you walk me through an example of topological sort in action?"*

</details>
