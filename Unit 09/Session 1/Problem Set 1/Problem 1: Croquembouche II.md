# Problem 1: Croquembouche II

You are designing a delicious croquembouche (a French dessert composed of a cone-shaped tower of cream puffs 😋), for a couple's wedding. They want the cream puffs to have a variety of flavors. You've finished your design and want to send it to the couple for review.

Given a root of a binary tree `design` where each node in the tree represents a cream puff in the croquembouche, traverse the croquembouche in tier order (i.e., level by level, left to right).

You should return a list of lists where each inner list represents a tier (level) of the croquembouche and the elements of each inner list contain the flavors of each cream puff on that tier (node `val`s from left to right).

**Note:** The `build_tree()` and `print_tree()` functions both use variations of a level order traversal. To get the most out of this problem, we recommend that you reference these functions as little as possible while implementing your solution.

Evaluate the time and space complexity of your function. Define your variables and provide a rationale for why you believe your solution has the stated time and space complexity. Assume the input tree is balanced when calculating time complexity.

*Hint: Level order traversal, BFS*

```python
class Puff():
     def __init__(self, flavor, left=None, right=None):
        self.val = flavor
        self.left = left
        self.right = right

def listify_design(design):
    pass
```

Example Usage:

```python
"""
            Vanilla
           /       \
      Chocolate   Strawberry
      /     \
  Vanilla   Matcha  
"""
croquembouche = Puff("Vanilla", 
                    Puff("Chocolate", Puff("Vanilla"), Puff("Matcha")), 
                    Puff("Strawberry"))
print(listify_design(croquembouche))
```

Example Output:

```markdown
[['Vanilla'], ['Chocolate', 'Strawberry'], ['Vanilla', 'Matcha']]
```

<br>

<details>
  <summary><strong>✨ AI Hint: Breadth First Search Traversal</strong></summary>

*Key Skill: Use AI to explain code concepts*

To solve this problem, it may be helpful to understand both the **queue** data structure and **breadth first search** algorithm. To learn more about these concepts, visit the Queues and Breadth First Search sections of the [Unit 9 Cheatsheet](https://courses.codepath.org/courses/tip103/unit/9#!cheatsheet)

If you still have questions, try explaining what you're doing, and ask an AI tool like ChatGPT or GitHub Copilot to help you understand what's confusing you. For example, you might ask:

*"I'm trying to understand how to use a queue to implement breadth first search, but I'm confused about why I wouldn't just use a list. Can you explain the difference?"*

</details>
