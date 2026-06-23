# Problem 1: Brand Filter

You're tasked with filtering out brands that are not sustainable from a list of fashion brands. A sustainable brand is defined as one that meets a specific criterion, such as using eco-friendly materials, ethical labor practices, or being carbon-neutral.

Write the `filter_sustainable_brands()` function, which takes a list of brands and a criterion, then returns a list of brands that meet the criterion.

Evaluate the time and space complexity of your solution. Define your variables and provide a rationale for why you believe your solution has the stated time and space complexity.

```
def filter_sustainable_brands(brands, criterion):
    pass
```

Example Usage:

```
brands = [
    {"name": "EcoWear", "criteria": ["eco-friendly", "ethical labor"]},
    {"name": "FastFashion", "criteria": ["cheap materials", "fast production"]},
    {"name": "GreenThreads", "criteria": ["eco-friendly", "carbon-neutral"]},
    {"name": "TrendyStyle", "criteria": ["trendy designs"]}
]

brands_2 = [
    {"name": "Earthly", "criteria": ["ethical labor", "fair wages"]},
    {"name": "FastStyle", "criteria": ["mass production"]},
    {"name": "NatureWear", "criteria": ["eco-friendly"]},
    {"name": "GreenFit", "criteria": ["recycled materials", "eco-friendly"]}
]

brands_3 = [
    {"name": "OrganicThreads", "criteria": ["organic cotton", "fair trade"]},
    {"name": "GreenLife", "criteria": ["recycled materials", "carbon-neutral"]},
    {"name": "FastCloth", "criteria": ["cheap production"]}
]

print(filter_sustainable_brands(brands, "eco-friendly"))
print(filter_sustainable_brands(brands_2, "ethical labor"))
print(filter_sustainable_brands(brands_3, "carbon-neutral"))
```

Example Output:

```
['EcoWear', 'GreenThreads']
['Earthly']
['GreenLife']
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
