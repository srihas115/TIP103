def longest_substring_without_repeating_characters(s):
    # seen = set
    
    # left starts at 0
    # longest = 0
    
    # for right in length of the string
    # if right not in seen
        # remove left from seen
        # add right to seen
    # longest = max(longest, right - left + 1)
    
    seen = set()
    
    left = 0
    longest = 0
    
    for right, char in enumerate(s):
        while char in seen:
            seen.remove(s[left])
            left += 1

        seen.add(char)
        longest = max(longest, right - left + 1)
    
    return longest

print("Example 1:")
s = "abcabcbb"
print("Expected: 3")
print("Actual: ", longest_substring_without_repeating_characters(s))

print()

print("Example 2:")
s = "bbbbb"
print("Expected: 1")
print("Actual: ",longest_substring_without_repeating_characters(s))

print()

print("Example 3:")
s = "pwwkew"
print("Expected: 3")
print("Actual: ",longest_substring_without_repeating_characters(s))