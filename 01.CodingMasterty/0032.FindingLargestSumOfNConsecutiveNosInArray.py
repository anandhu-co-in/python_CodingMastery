# Given you have an array, you need to find the largest sum of n consecutive numbers in it


array = [2, 6, 9, 2, 1, 8, 5, 6, 3]
n = 3

def findMaxConsecutiveSum(arr, n):

    if n>len(arr):
        return "Error, array doesnt have {} elements".format(n)
    i = 0
    j = 0
    maxSum = 0

    while j < n:
        maxSum = maxSum + arr[j]
        j = j + 1
        print("here")
    windowsSum=maxSum
    while j < len(array):
        print(i,j)
        windowsSum=windowsSum + arr[j] - arr[i]
        print("Added {} and substracted {} to get {}".format(arr[j],arr[i],windowsSum))
        maxSum = max(maxSum,windowsSum)
        j = j + 1
        i = i + 1
    return maxSum

print(findMaxConsecutiveSum(array, n))
