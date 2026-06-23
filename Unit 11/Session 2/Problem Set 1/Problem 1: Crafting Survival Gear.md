# Problem 1: Crafting Survival Gear

In the aftermath of the zombie apocalypse, your survival depends on crafting essential gear from limited resources. You are given a list of strings, `gear` that you can craft and a 2D list `components` where `components[i]` contains the materials you need to craft `gear[i]`. 

Some components are basic supplies that you already have, while others need to be crafted from other gear. Additionally, you are given a string array `supplies` containing all the components you initially have in your stash (infinite supply). 

Return a list of all the gear you can craft. You can return the list in any order.

```python
def craftable_gear(gear, components, supplies):
    pass
```

Example Usage: 

```python
gear_1 = ["weapon"]
components_1 = [["metal", "wood"]]
supplies_1 = ["metal", "wood", "rope"]

gear_2 = ["weapon", "trap"]
components_2 = [["metal", "wood"], ["weapon", "wire"]]
supplies_2 = ["metal", "wood", "wire"]

gear_3 = ["weapon", "trap", "shelter"]
components_3 = [["metal", "wood"], ["weapon", "wire"], ["trap", "wood", "metal"]]
supplies_3 = ["metal", "wood", "wire"]

print(craftable_gear(gear_1, components_1, supplies_1))
print(craftable_gear(gear_2, components_2, supplies_2))
print(craftable_gear(gear_3, components_3, supplies_3))
```

Example Output: 

```markdown
["weapon"]
Example 1 Explanation: You can craft "weapon" since you have the components "metal" and "wood" in your stash.

["weapon", "trap"]
Example 2 Explanation:
- You can craft "weapon" first since you have "metal" and "wood."
- After crafting "weapon", you can craft "trap" since you have "wire" and the "weapon" you just crafted.

["weapon", "trap", "shelter"]
Example 3 Explanation: 
- You can craft "weapon" first.
- With the "weapon" and "wire", you can craft "trap."
- With the "trap", "wood", and "metal," you can craft "shelter."
```

<details>
  <summary><strong>✨ AI Hint: Topological Sort</strong></summary>

*Key Skill: Use AI to explain code concepts*

This problem may be solved with topological sort. Check out the Advanced section of the [Unit 11 Cheatsheet](https://courses.codepath.org/courses/tip103/unit/11#!cheatsheet) for more information.

If you need more info, you can ask an AI tool like ChatGPT or GitHub Copilot to help you understand topological sort. For example, you can ask:

*"What is topological sort, and when is it useful for solving coding problems?"*

*"Can you walk me through an example of topological sort in action?"*

</details>
