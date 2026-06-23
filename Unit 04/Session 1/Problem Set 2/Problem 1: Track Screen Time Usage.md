# Problem 1: Track Screen Time Usage

In the digital age, managing screen time is crucial for maintaining a healthy balance between online and offline activities. You need to track how much time users spend on different apps throughout the day.

Write the`track_screen_time()`function, which takes a list of logs, where each log contains an app name and the number of minutes spent on that app during a specific hour. The function should return the app names and the total time spent on each app.

Evaluate the time and space complexity of your solution. Define your variables and provide a rationale for why you believe your solution has the stated time and space complexity.

```
def track_screen_time(logs):
    pass
```

Example Usage:

```
logs = [("Instagram", 30), ("YouTube", 20), ("Instagram", 25), ("Snapchat", 15), ("YouTube", 10)]
logs_2 = [("Twitter", 10), ("Reddit", 20), ("Twitter", 15), ("Instagram", 35)]
logs_3 = [("TikTok", 40), ("TikTok", 50), ("YouTube", 60), ("Snapchat", 25)]

print(track_screen_time(logs))
print(track_screen_time(logs_2))
print(track_screen_time(logs_3))
```

Example Output:

```
{'Instagram': 55, 'YouTube': 30, 'Snapchat': 15}
{'Twitter': 25, 'Reddit': 20, 'Instagram': 35}
{'TikTok': 90, 'YouTube': 60, 'Snapchat': 25}
```

## 💡 Hint: Big O (Time & Space Complexity)
Big O notation is a mathematical notation in computer science used to describe the the time and space complexity of an algorithm. Time complexity is the amount of time an algorithm or function takes to run in comparison to the size of the input data. Space complexity is the amount of extra memory or space an algorithm or function needs to complete its task in comparison to the size of the input data.

For your convenience, we've included a summary of the three most common Big O functions below.

Common Big O includes:

-   **O(1) - Constant Time** No matter the size of your input data, the function takes a fixed amount of time or memory to complete its task.

    Example: Summing two numbers

    ```
    def sum(a, b):
        return a + b
    ```

    It takes the computer roughly the same amount of time to sum `a` and `b` no matter how large the two numbers are.

-   **O(n) - Linear Time** The amount of time or memory your function needs grows linearly with the size of your input data.

    Example: Printing each item in a list

    ```
    def print_list(lst):
        for item in lst:
            print(item)
    ```

    The computer has to perform one extra print statement for each extra item there is in the list, so the length of time it takes to print the list will be proportional to the number of items in the list. We expect that it will take 1000 times longer to print a list with 1000 elements than it will to print a list with just 1 element.

-   **O(n²) - Quadratic Time** The amount of time or memory your function needs grows quadratically with the size of your input data.

    Example: Finding Duplicates Using a Nested For Loop

    ```
    def find_duplicates(lst):
        n = len(lst)
        for i in range(n):
            for j in range(i + 1, n):
                if lst[i] == lst[j]:
                    print(f"Duplicate found: {lst[i]}")
                    return True
        return False
    ```

    The function compares each element in the list to every other element in the list, which means we perform roughly n² comparisons where n is the length of our input list `lst`, so it will take n² time to complete all comparisons. We can expect that for a list of size 2, we will perform roughly 4 comparisons whereas for a list of size 10 we will perform roughly 100 comparisons.

## AI Hint: Decoding Big O
*Key Skill: Use AI to explain code concepts*

Big O is a big topic, and kind of tricky to wrap your head around! If you're feeling confused, try asking an AI tool like ChatGPT or GitHub Copilot to explain it to you:

*"You're an expert computer science tutor for a Python-based technical interviewing prep course. Can you use an analogy to help me understand Big O notation? Please explain the concept of time and space complexity in a way that is easy to understand."*

Once it gives you an answer, you can ask follow-up questions to clarify any points that are still confusing. Be patient with yourself, and remember that this is a complex topic that takes time to fully understand!