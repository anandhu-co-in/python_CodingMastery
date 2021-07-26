def lengthOfLongestSubstring2(s):
    """
    :type s: str
    :rtype: int
    """

    p1 = 0
    p2 = 0

    ans = 0

    dic = {}

    while p2 < len(s):

        if s[p2] in dic and dic[s[p2]] >= p1:
            p1= dic[s[p2]]+1
        else:
            dic[s[p2]] = p2
            ans = max(ans, 1 + p2 - p1)
            p2 = p2 + 1

    return ans


print(lengthOfLongestSubstring2("abcabcbb"))


def longestPalindrome(s):
    ans = 0

    ansstring = ""

    for i in range(len(s)):

        p1 = p2 = i

        if p1 + 1 < len(s) and s[p1] == s[p1 + 1]:
            p2 = p1 + 1

        while (p1 >= 0 and p2 < len(s)) and (s[p1] == s[p2]):
            if p2 - p1 + 1 > ans:
                ans = p2 - p1 + 1

                ansstring = s[p1:p2 + 1]

            p1 -=1
            p2 += 1

    return ansstring



print(longestPalindrome("ccc"))


