
def pivot(arr,left,right):

    swapIndex=left
    i=left+1
    pivot=arr[left]
    print("Left = "+str(left)+" Right = "+str(right)+" pivot is "+str(pivot))
    while(i<=right):
        if(arr[i]<pivot):
            swapIndex=swapIndex+1
            arr[i],arr[swapIndex]=arr[swapIndex],arr[i]
        i=i+1

    arr[left], arr[swapIndex] = arr[swapIndex], arr[left]

    print("-----------------------------------> "+str(arr))
    return(swapIndex)

def quickSort(arr,left='',right=''):

    if left=='':
        left=0
    if right=='':
        right=len(arr)-1

    if(left>=right):
        return arr
    p=pivot(arr,left,right)

    quickSort(arr,left,p-1)
    quickSort(arr,p+1,right)

    return arr

quickSort([744,1,5,2,6,8,2,6,7,4,88,6,5,7,4,6,6,5,6,7,4,5,7,6,4,3,744])



#O(nlogn)