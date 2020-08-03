#Given an array, find if there is a sub array with specific sum

#I came up with this recursive solution on myown, though it took hours, i felt the happiness
#Unfortunately this is a horrible solution in terms of time complexity. 2^n i guess
#For longer arrays it takes forever! Please check the version with dynamic programmming

def findsum(array):
    sum=0
    for i in array:
        sum=sum+i
    return sum

def hassubArrayWithSum(array,sum):
    print("Checking {} for sum {}".format(array,sum))
    if findsum(array)==sum:
        return [True,array]
    elif len(array)==1 or findsum(array)<sum:
        return False
    else:
        for i in array:
            if i==sum:
                return [True,[i]]
            else:
                temparray=array.copy()
                temparray.remove(i)
                if sum-i>0:
                    temp=hassubArrayWithSum(temparray,sum-i)
                    if temp!=False:
                        return [True,[i]+temp[1]]
        return False

array=[3,2,8,5,1,2,3,4,5,6]
print(hassubArrayWithSum(array,40))
print(hassubArrayWithSum(array,20))




#Below is a BETTER recursive solution from. Now i realized how pathetic my recursive solution was,, haha  (But still need to figureout how get the subarray like I DID :

print("\n\nOther solution from NET : ")

def isSubsetSum(set, n, sum):

    # Base Cases
    if (sum == 0):
        return True

    if (n == 0 and sum != 0):
        return False

    # If last element is greater than sum, then ignore it
    if (set[n - 1] > sum):
        return isSubsetSum(set, n - 1, sum);

    # else, check if sum can be obtained by any of the following (a) including the last element (b) excluding the last element  # i think it is Excluding and including respectively below
    return isSubsetSum(set, n - 1, sum) or isSubsetSum(set, n - 1, sum - set[n - 1])

# Driver program to test above function
set = [3, 34, 4, 12, 5,2,3,5,4,6,7,2,5,3,5,7,3,6,2,6,7,3]
sum = 10

if (isSubsetSum(set, len(set), sum) == True):
    print("Found a subset with given sum")
else:
    print("No subset with given sum")




