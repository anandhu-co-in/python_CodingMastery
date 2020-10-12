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
            start = mid + 1
        elif arr[mid] == 0:
            end = end - 1

        mid = math.floor((start + end) / 2)

    print(len(arr) - mid - 1)
