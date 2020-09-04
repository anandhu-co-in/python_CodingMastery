# Write a function called findLongestSubstringWithDistinctChars which acceptes a string and returns the length of the longest
# substring with all distincts charectors


def findLongestSubstringWithDistinctChars(str):
    pointer1 = 0
    maxLen = 0
    seen = {}
    i = 0
    while i < len(str):
        c = str[i]
        # print("char {}".format(c))
        if seen.get(c) is not None:
            pointer1 = max(pointer1, seen[c] + 1) # <--- Explanation below!
        maxLen = max(maxLen, i - pointer1 + 1)
        seen[c] = i
        i = i + 1
    return maxLen


print(findLongestSubstringWithDistinctChars(''))  # 0
print(findLongestSubstringWithDistinctChars('rithmschool'))  # 7
print(findLongestSubstringWithDistinctChars('thisisawesome'))  # 6
print(findLongestSubstringWithDistinctChars('thecatinthehat'))  # 7
print(findLongestSubstringWithDistinctChars('bbbbbb'))  # 1
print(findLongestSubstringWithDistinctChars('longestsubstring'))  # 8
print(findLongestSubstringWithDistinctChars('thisishowwedoit'))  # 6

# I had a confusion about the max logic and after Brainstorming :  since seen dic always has the latest position
# value, But the pointer can be moved forward bcs of another characters repetition earlier, That's why max logic is
# still needed ! like in this case abcXeYghYjkXmnopqr, on second occurrence of  Y pointer1 is moved after first Y. In
# second occurrence of X pointer1 should NOT be brought after first X!
