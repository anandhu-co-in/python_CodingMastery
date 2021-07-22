# https://leetcode.com/problems/reverse-integer/

# My Solution

def reverse( x):
    rev = 0
    negative = False
    if (x < 0):
        negative = True
        x = x * -1
    while (x > 0):
        rev = rev * 10 + x % 10
        x = x // 10
    if (rev > 2 ** 31 or (negative and rev > 2 ** 31 - 1)):
        return 0
    if negative:
        return rev * -1
    return rev

print(reverse(-767345))