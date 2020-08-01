


def searchLinear(arr,key):
    for i in range(len(arr)):
        print(arr[i])
        if arr[i]==key :
            print("Found at position "+str(i+1))
            return
    print("Not found :-(")

arr=[1,2,3,4,5,6,7,8,9]
searchLinear(arr, 7)