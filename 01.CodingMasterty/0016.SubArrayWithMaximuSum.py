# Fond the sub array(contiguos) maximum sum in a give array, Dont confuse with the subset sum problems, here we are looking for subarray with contiguous elements
# https://www.youtube.com/watch?v=86CQq3pKSUw


# Brute Force Method
def findSubArrayWithMaxSumBruteForce(array):
    steps = 0

    largest = [0]

    for i in range(len(array)):
        for j in range(i, len(array)):
            steps += 1
            subArray = array[i:j + 1]
            # I learned that last index in not inclusive, ie arr[0:4], will include from 0th index to 3rd index
            print("Found sub array {} with sum {}".format(subArray, sum(subArray)))
            if sum(subArray) > sum(largest):
                largest = subArray

    print("Largest Sum sub array using BruteForce is {} with sum {}".format(largest, sum(largest)))

array = [-2, -3, 4, -1, -2, 1, 5, -3]
findSubArrayWithMaxSumBruteForce(array)


# Optimal Solution Using Kadanes Algorithm :
def findMaxSubArrayKadanes(array):

    size = len(array)
    result=array[0]
    currentMax = array[0]
    for i in range(1, size):
        currentMax=max(array[i],currentMax+array[i])
        result=max(currentMax,result)

    print("\nMaximum sum using Kadanes Algorithm --> {}".format(result))

array = [-2, -3, 4, -1, -2, 1, 5, -3]
findMaxSubArrayKadanes(array)