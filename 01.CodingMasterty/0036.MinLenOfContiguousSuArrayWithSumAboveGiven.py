# Write a function called minSubArrayLen which accepts two parameters - an array of positive integers and a positive
# integer The function should return the minimal length of a contiguous sub array of which the sum is greater than or
# equal to the integers passed to the function. If there isn't one return 0 instead
import math


def minSubArrayLen(array, sum):
    pointer1=0
    pointer2=0
    currentSum=array[0]

    minLen=math.inf

    while(pointer1<=pointer2):
        if currentSum<sum and pointer2<len(array)-1:
            pointer2=pointer2+1
            currentSum=currentSum+array[pointer2]

        elif(currentSum>=sum):
            minLen=min(minLen,pointer2-pointer1+1)
            currentSum=currentSum-array[pointer1]
            pointer1 = pointer1 + 1
        else:
            break

    if minLen == math.inf:
        return 0
    else:
        return minLen


print(minSubArrayLen([2, 3, 1, 2, 4, 3], 7))
print(minSubArrayLen([2, 1, 6, 5, 4], 9))  # 2 -> because [5,4] is the smallest subarray
print(minSubArrayLen([3, 1, 7, 11, 2, 9, 8, 21, 62, 33, 19], 52))  # 1 -> because [62] is greater than 52
print(minSubArrayLen([1, 4, 16, 22, 5, 7, 8, 9, 10], 39))  # 3
print(minSubArrayLen([1, 4, 16, 22, 5, 7, 8, 9, 10], 55))  # 5
print(minSubArrayLen([4, 3, 3, 8, 1, 2, 3], 11))  # 2
print(minSubArrayLen([1, 4, 16, 22, 5, 7, 8, 9, 10], 95))  # 0



