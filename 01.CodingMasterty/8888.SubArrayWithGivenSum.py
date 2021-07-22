

def findSubArrayGivenSum(arr,sum):

    left=0
    right=0
    currentSum=0


    while left<len(arr) and right <len(arr):

        currentSum = currentSum + arr[right]


        if currentSum<sum:

            right=right+1

        elif(currentSum>sum):

            currentSum = currentSum - arr[left]
            left+=1

        else:
            if sum == currentSum:
                print(left, right)
                return



findSubArrayGivenSum([1,2,3,4,5],10)





