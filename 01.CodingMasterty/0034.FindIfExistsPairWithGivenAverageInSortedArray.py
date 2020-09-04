# Given a sorted array, find if there exists a pair of elements with a given average


def checkIfAveragePairExists(array, avg):
    sum = avg * 2

    pointer1 = 0
    pointer2 = len(array) - 1

    while pointer1 < pointer2:

        currentSum=array[pointer1] + array[pointer2]

        if currentSum == sum:
            return True
        elif(currentSum<sum):
            pointer1=pointer1+1
        else:
            pointer2=pointer2-1

    return False

# Expected answer on comment
print(checkIfAveragePairExists([1, 2, 3], 2.5))  # True
print(checkIfAveragePairExists([1, 3, 3, 5, 6, 7, 10, 12, 19], 8))  # True
print(checkIfAveragePairExists([-1, 0, 3, 4, 5, 6], 4.1))  # False
print(checkIfAveragePairExists([], 4))  # False
