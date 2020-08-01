# Count of ways to make Array sum even by removing only one element
# Given an array arr[] positive integers, the task is to find the number of ways to convert the array sum even if we are allowed to remove only one element.
#
# Examples:
#
# Input: arr[] = { 1, 3, 3, 2 }
# Output: 3
# Explanation:
# 1. Remove 1, then sum is 3 + 3 + 2 = 8.
# 2. Remove 3, then sum is 1 + 3 + 2 = 6.
# 3. Remove 3, then sum is 1 + 3 + 2 = 6.
#
# Input: arr[] = { 4, 8, 3, 3, 6 }
# Output: 3
# Explanation:
# 1. Remove 4, then sum is 8 + 3 + 3 + 6 = 20.
# 2. Remove 8, then sum is 4 + 3 + 3 + 6 = 16.
# 3. Remove 6, then sum is 4 + 8 + 3 + 3 = 18.

# https://www.geeksforgeeks.org/count-of-ways-to-make-array-sum-even-by-removing-only-one-element/


#This is how i wrote - Correct solution is after this!! I need to think

def noOfWaysToMakeEvenByOneElementRemoval(array):
    total=sum(array)
    count=0

    for x in array:
        if (total-x)%2==0:
            count+=1
    return count



print(noOfWaysToMakeEvenByOneElementRemoval([4,8,3,3,6]))



#As always, i should have thought more!

# If we have an odd number of odd elements then the sum is always odd then we have to remove one odd number from the array arr[] to make the sum even.
# Since we have to remove one element, therefore, the total number of ways of making the sum even is the count of odd elements in the array arr[].
# If we have an even number of odd elements then the sum is always even. Since we have to remove one element to make the sum even, therefore,
# the total number of ways of making the sum even is the count of even elements in the array arr[]

def noOfWaysToMakeEvenByOneElementRemoval(array):





    #even number of odd numbers - > sum is now odd, I can remove any even numner


    #if i have odd no of odd nos --> sum is odd ---> i can remove any odd numver

    oddCount=0
    EvenCount=0

    for num in array:
        if num%2==0:
            EvenCount+=1
        else:
            oddCount+=1

    if oddCount%2==0:
        return EvenCount
    else:
        return oddCount


print(noOfWaysToMakeEvenByOneElementRemoval([4,8,3,3,6]))
















