# Given a sorted array. write snippet that finds the count of unique values in it

array = [1, 2, 3, 4, 4, 4, 7, 7, 12, 12, 13, 14]


# My approach
def countUniqueNos(arr):
    uniqueCount = 1
    if len(array) == 0:
        return 0
    if len(array) == 1:
        return 1
    prev = 0
    i = 1
    while i < len(array):
        if array[i] != array[prev]:
            uniqueCount = uniqueCount + 1
        prev = prev + 1
        i = i + 1

    return uniqueCount


print(countUniqueNos(array))


# CorrectApproch form the udemy guy's solution
# Point i at first charector, and j at second
# If j becomes difference from i , move i right and place the j value there!
def countUniquesUdemySol(arr):
    if len(arr) == 0:
        return 0
    else:
        i = 0
        j = 1
        while j < len(array):
            if arr[i] != arr[j]:
                i = i + 1
                arr[i] = arr[j]
            j = j + 1
        return i + 1


print(countUniquesUdemySol(array))

# i think this approch is better, because in the while loop, we only increment j unless the values mismatch
# in the former solution, inside the while loop, i was incrementing both the pointer i used, on every iteration. bad me!
