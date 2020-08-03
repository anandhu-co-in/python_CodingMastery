
#Divide and Conquer on Sorted Array!
from math import floor


def searchBinary(arr,key):
    start=0
    end=len(arr)-1
    mid=int((start+end)/2)
    while(start<=end):
        if key==arr[mid] :
            print("Found at position "+str(mid+1))
            return
        else:
            if key>arr[mid]: start=mid+1
            else:end=mid-1
            mid = floor((start + end) / 2)
            print(arr[mid])
    print("Nod Found :-(")

arr=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]

searchBinary(arr,16)


