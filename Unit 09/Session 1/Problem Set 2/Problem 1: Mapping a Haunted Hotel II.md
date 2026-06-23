# Problem 1: Mapping a Haunted Hotel II

You have been working the night shift at a haunted hotel and guests have been coming to check out of rooms that you're pretty sure don't exist in the hotel... or are you imagining things? To make sure, you want to explore the entire hotel and make your own map.

Given the root of a binary tree `hotel` where each node represents a room in the hotel, write a function `map_hotel()` that returns a dictionary mapping each level of the hotel to a list with the level's room values in the order they appear on that level from left to right. 

Evaluate the time and space complexity of your function. Define your variables and provide a rationale for why you believe your solution has the stated time and space complexity. Assume the input tree is balanced when calculating time complexity.

**Note:** The `build_tree()` and `print_tree()` functions both use variations of a level order traversal. To get the most out of this problem, we recommend that you reference these functions as little as possible while implementing your solution. 

```python
class TreeNode():
    def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right

def map_hotel(hotel):
    pass
```

Example Usage:

```python
"""
         Lobby
        /     \
       /       \
      101      102
     /   \    /   \
   201  202  203  204
   /                \ 
 301                302
"""

hotel = Room("Lobby", 
                Room(101, Room(201, Room(301)), Room(202)),
                Room(102, Room(203), Room(204, None, Room(302))))

print(map_hotel(hotel))
```

Example Output:

```markdown
{
    0: ['Lobby'],
    1: [101, 102],
    2: [201, 202, 203, 204],
    3: [301, 302]
}
```

<br>

<details>
  <summary><strong>✨ AI Hint: Breadth First Search Traversal</strong></summary>

*Key Skill: Use AI to explain code concepts*

To solve this problem, it may be helpful to understand both the **queue** data structure and **breadth first search** algorithm. To learn more about these concepts, visit the Queues and Breadth First Search sections of the [Unit 9 Cheatsheet](https://courses.codepath.org/courses/tip103/unit/9#!cheatsheet)

If you still have questions, try explaining what you're doing, and ask an AI tool like ChatGPT or GitHub Copilot to help you understand what's confusing you. For example, you might ask:

*"I'm trying to understand how to use a queue to implement breadth first search, but I'm confused about why I wouldn't just use a list. Can you explain the difference?"*

</details>
