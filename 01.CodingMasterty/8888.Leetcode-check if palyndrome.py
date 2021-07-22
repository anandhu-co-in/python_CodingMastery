# https://leetcode.com/problems/palindrome-number/


def isPalindrome(x):
    x = str(x)

    start = 0
    end = len(x) - 1

    while (start <= end):
        if (x[start] != x[end]):
            return False
        start = start + 1
        end = end - 1

    return True


print(isPalindrome(-244))
print(isPalindrome(123454321))
print(isPalindrome(666))
print(isPalindrome(0))