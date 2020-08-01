def insertionSort(arr):
    for i in range(1,len(arr)):   #loop from second element ie index 1 to end
        currentVal=arr[i]
        j = i - 1
        while(j>=0 and currentVal<arr[j]):
            arr[j+1] = arr[j]
            j=j-1
        arr[j+1]=currentVal
    return arr


print(insertionSort([9,8,5,6,4,3,2,1]))


#Time complexity is O(n)