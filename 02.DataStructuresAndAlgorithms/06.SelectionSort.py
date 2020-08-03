def selectionSort(arr):
    for i in range(len(arr)):   #lop from 0 to end, 1 to end so on..
        lowest=i
        for j in range(i+1,len(arr)):
            if(arr[j]<arr[lowest]):
                lowest=j
        if(i!=lowest):  #To optimize. No need to swap if old the first one itself is largest
            arr[i], arr[lowest] = arr[lowest], arr[i]
    return arr


print(selectionSort([7,5,4,6,2,9,3,7,3,5,7,0,1,2,3]))


#time complexity : O(n2)














# // LEGACY VERSION (non ES2015 syntax)
# function sselectionSort(arr){
#     for(var i = 0; i < arr.length; i++){
#         var lowest = i;
#         for(var j = i+1; j < arr.length; j++){
#             if(arr[j] < arr[lowest]){
#                 lowest = j;
#             }
#         }
#         if(i !== lowest){
#             //SWAP!
#             var temp = arr[i];
#             arr[i] = arr[lowest];
#             arr[lowest] = temp;
#         }
#     }
#     return arr;
# }




