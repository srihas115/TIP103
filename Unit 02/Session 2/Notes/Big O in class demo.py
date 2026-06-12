import time


# Complexity    Typical Pattern                             Example Problem
# O(1)          Direct access                               arr[0]
# O(log n)      Halve the search space                      Binary Search
# O(n)          One pass through data                       Find max
# O(n log n)    Divide-and-conquer + process all elements   Merge Sort
# O(n²)         Nested loops over same data                 Compare every pair
# O(2ⁿ)         Include/exclude decisions                   Generate all subsets
# O(n!)         Try every ordering                          Generate all permutations


# O(1)
def constant_example(arr):
    return arr[0]




# O(log n)
def logarithmic_example(n):
    while n > 1:
        n //= 2




# O(n)
def linear_example(arr):
    for item in arr:
        pass




# O(n log n)
def log_linear_example(arr):
    sorted(arr)




# O(n²)
def quadratic_example(arr):
    for i in arr:
        for j in arr:
            pass




# O(2^n)
def exponential_example(n):
    if n == 0:
        return 1


    return (
        exponential_example(n - 1)
        + exponential_example(n - 1)
    )




# O(n!)
def factorial_example(arr, start=0):
    if start == len(arr):
        return


    for i in range(start, len(arr)):
        arr[start], arr[i] = arr[i], arr[start]


        factorial_example(arr, start + 1)


        arr[start], arr[i] = arr[i], arr[start]




def benchmark(name, func, *args):
    start = time.perf_counter()


    func(*args)


    elapsed = time.perf_counter() - start


    print(f"{name:<20} {elapsed:.8f} seconds")


def longest_substring_without_repeating_characters(s):
    seen = set()
    left = 0
    longest = 0
    for right in range(len(s)):
        while s[right] in seen:
            seen.remove(s[left])
            left += 1


        seen.add(s[right])
        longest = max(longest, right - left +1)


    print(longest)
    # left starts at 0
    # lonngest = 0


    # for right in len of string
    # While right is seen
    # Remove left from seen
    # move left to right
    # if right not in seen
    #add right to seen
    # longest = max(longesst, right - left +1)


    return longest




def main():
    longest_substring_without_repeating_characters("abcabcbb")
    longest_substring_without_repeating_characters("bbbbb")
    longest_substring_without_repeating_characters("pwwkew")


    print("Runtime Demonstrations")
    print("-" * 40)


    benchmark(
        "O(1)",
        constant_example,
        list(range(1_000_000))
    )


    benchmark(
        "O(log n)",
        logarithmic_example,
        1_000_000
    )


    benchmark(
        "O(n)",
        linear_example,
        list(range(1_000_000))
    )


    benchmark(
        "O(n log n)",
        log_linear_example,
        list(range(100_000, 0, -1))
    )


    benchmark(
        "O(n²)",
        quadratic_example,
        list(range(2_000))
    )


    benchmark(
        "O(2^n)",
        exponential_example,
        20
    )


    benchmark(
        "O(n!)",
        factorial_example,
        [1, 2, 3, 4, 5, 6, 7,8 ,9 ,10,11,12,13]
    )






if __name__ == "__main__":
    main()
    #258 seconds

