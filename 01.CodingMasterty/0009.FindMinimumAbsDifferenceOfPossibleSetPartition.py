# https://www.geeksforgeeks.org/amazon-interview-experience-sde-1-amazon-wow-2020/?ref=leftbar-rightbar
# 3. Given an array and split the array into two halves such that the absolute difference between them should be minimum.
#
# Ex : 37, 43, 7, 54
#
# o/p = (37+43) – (54+7) = 19
from math import floor


def show(matrix):
    for i in matrix:
        print(i)

def findsum(array):
    sum=0
    for i in array:
        sum=sum+i
    return sum

def findMinPartitionDifference(array):

    sumofArray=findsum(array)
    sum=floor(sumofArray/2)

    if len(array)==0:
        return "Array Empty"

    matrix=[[False for x in range(sum+1)] for x in range(len(array))]

    for i in range(len(array)):
        matrix[i][0]=True

    for j in range(1,sum+1):
        if array[0]==j:
            matrix[0][j]=True
        else:
            matrix[0][j] = False

    for i in range(1,len(array)):
        for j in range(1,sum+1):
            if matrix[i-1][j] ==True:
                matrix[i][j]=True
            elif j>=array[i]:
                matrix[i][j]=matrix[i-1][j-array[i]]
    show(matrix)

    partition1=0
    i=len(array)-1
    j=sum
    while j>0:
        if matrix[i][j]==True:
            partition1=j
            break
        j=j-1

    partition2=sumofArray-partition1
    return abs(partition2-partition1)

array=[37, 43, 7, 54]
print(findMinPartitionDifference(array))
