# Problem 5: Filter Records by Waste Threshold

You are given a list of food waste records, where each record is a tuple consisting of a date (in the format `"YYYY-MM-DD"`) and an integer representing the amount of food wasted on that date. You are also given a waste threshold. Your task is to filter out and return a list of tuples with only the records where the waste amount is greater than or equal to the threshold.

Evaluate the time and space complexity of your solution. Define your variables and provide a rationale for why you believe your solution has the stated time and space complexity.

```python
def filter_records_by_waste_threshold(waste_records, threshold):
  pass
```

Example Usage:

```python
waste_records1 = [
    ("2024-08-01", 150),
    ("2024-08-02", 200),
    ("2024-08-03", 50),
    ("2024-08-04", 300),
    ("2024-08-05", 100),
    ("2024-08-06", 250)
]
threshold1 = 150

result = filter_records_by_waste_threshold(waste_records1, threshold1)
print(result)

waste_records2 = [
    ("2024-07-01", 90),
    ("2024-07-02", 120),
    ("2024-07-03", 80),
    ("2024-07-04", 130),
    ("2024-07-05", 70)
]
threshold2 = 100

result = filter_records_by_waste_threshold(waste_records2, threshold2)
print(result)
```

Example Output:

```markdown
[('2024-08-01', 150), ('2024-08-02', 200), ('2024-08-04', 300), ('2024-08-06', 250)]
[('2024-07-02', 120), ('2024-07-04', 130)]
```
