#https://www.geeksforgeeks.org/number-of-ways-to-get-a-given-sum-with-n-number-of-m-faced-dices/
# Given n dices each with m faces, numbered from 1 to m, find the number of ways to get a given sum X. X is the summation of values on each face when all the dice are thrown.
#
# Examples:
#
# Input : faces = 4 throws = 2 sum =4
# Output : 3
# Ways to reach sum equal to 4 in 2 throws can be { (1, 3), (2, 2), (3, 1) }
#
# Input : faces = 6 throws = 3 sum = 12
# Output : 25

# 4 face ull dice, 2, pravahsaym erinju,  3 reethiyil 4 kiitaaam
# we need to findout, all permutation of 1-4 that can give that sum

# import math




#I doubt if i was realy able to think this ones DP logic,, hahaha



faces=6
throws=3
sum=12



matrix = [[None for x in range(sum+1)] for y in range(throws+1)]

def prinmatrix():

    for i in matrix:
        print(i)

prinmatrix()



def findNoOfWays(faces,throws,sum):

    if throws==0 and sum==0:
        return 1
    if throws == 0 or sum<0:
        return 0

    if matrix[throws][sum] is not None:
        return matrix[throws][sum]
    else:
        a=0
        for i in range(1,faces+1):
           a=a+findNoOfWays(faces,throws-1,sum-i)

        matrix[throws][sum] = a
        print("{} can be achieved in {} ways using {} throws".format(sum,a,throws))
        return a

print(findNoOfWays(faces,throws,sum))


