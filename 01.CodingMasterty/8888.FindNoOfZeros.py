# Give an array of 1s followed by 0s, find the no of 0s in it
import math

# arr = [1, 1, 1, 1, 0, 0, 0, 0, 0]
arr = [1,1,0,0,0,0,0]


start = 0
end = len(arr) - 1
if len(arr) == 0 or arr[len(arr) - 1] == 1:
    print(0)
elif arr[0] == 0:
    print(len(arr))
else:
    mid = math.floor((start + end) / 2)
    while not (arr[mid] == 1 and arr[mid + 1] == 0):

        if arr[mid + 1] == 1:
            start = mid
        elif arr[mid] == 0:
            end = mid

        mid = math.floor((start + end) / 2)

    print(len(arr) - mid - 1)





# function countZeroes(arr){
#    var n=arr.length;
#    var start=0;
#    var end=n-1;
#
#    if(n==0){
#        return 0;
#    }
#
#    if(arr[n-1]==1){
#        return 0;
#    }
#
#    if(arr[0]==0){
#        return n;
#    }
#
#    var mid=Math.floor((start+end)/2);
#    while (start<=end && !(arr[mid]==1 && arr[mid+1]==0)){
#        1234;
#
#        if(arr[mid+1]==1){
#            start=mid;
#        }
#        else{
#            end=mid;
#        }
#     mid=Math.floor((start+end)/2);
#
#    }
#
# return n-mid-1;
#
# }