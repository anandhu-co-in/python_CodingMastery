from math import floor


def merge(arr1, arr2):
    result = []
    i = 0
    j = 0

    while (i < len(arr1) and j < len(arr2)):

        if (arr1[i] < arr2[j]):
            result.append(arr1[i])
            i = i + 1
        else:
            result.append(arr2[j])
            j = j + 1

    while (i < len(arr1)):
        result.append(arr1[i])
        i = i + 1

    while (j < len(arr2)):
        result.append(arr2[j])
        j = j + 1

    print("Merged arrays " + str(arr1) + " and " + str(arr2) + " to " + str(result))
    return result


def mergeSort(arr):
    if (len(arr) <= 1):
        return arr
    else:
        print(str(arr) + " splitted to " + str(arr[:floor(len(arr) / 2)]) + " and " + str(arr[floor(len(arr) / 2):]))
        return merge(mergeSort(arr[:floor(len(arr) / 2)]), mergeSort(arr[floor(len(arr) / 2):]))


print(mergeSort([5, 6, 4, 7, 3, 8, 2, 9, 1]))


#O(nlongn)