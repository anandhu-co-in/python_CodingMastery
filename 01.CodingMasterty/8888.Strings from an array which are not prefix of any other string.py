# https://www.geeksforgeeks.org/strings-from-an-array-which-are-not-prefix-of-any-other-string/
# Given an array arr[] of strings, the task is to print the strings from the array which are not prefix of any other string from the same array.
#
# Examples:
#
# Input: arr[] = {“apple”, “app”, “there”, “the”, “like”}
# Output:
# apple
# like
# there
# Here “app” is a prefix of “apple”
# Hence, it is not printed and
# “the” is a prefix of “there”
#
# Input: arr[] = {“a”, “aa”, “aaa”, “aaaa”}
# Output:
# aaaa


def printAllNonePrefixOnes(arr):

    n=len(arr)

    for i in range(0,n):
        include=True
        for j in range(i+1,n):
            if arr[j].startswith(arr[i]):
                include=False
                break
        if include:
            print("{} exists ".format(i))
            print(arr)
            arr.remove(arr[i])
            n=n-1

    print(arr)



printAllNonePrefixOnes(['apple', 'app', 'there', 'the', 'like'])








