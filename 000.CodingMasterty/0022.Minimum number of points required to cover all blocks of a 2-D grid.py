# #https://www.geeksforgeeks.org/minimum-number-of-points-required-to-cover-all-blocks-of-a-2-d-grid/
#
#
# Given two integers N and M. The task is to find the minimum number of points required to cover an N * M grid.
#
# A point can cover two blocks in a 2-D grid when placed in any common line or sideline.
#
# Examples:
#
# Input: N = 5, M = 7
# Output: 18
#
# Input: N = 3, M = 8
# Output: 12




#Solution - Actually I ddidnt do it on my own, I should have, anyway
#if n*m is odd, then we have n/2 and + 1 ponts, other wise n/1
#Have to Learn About Greedy Algorithms



def prinMinPoints(m,n):

    if (m*n)%2==0:
        print (int(m*n/2))
    else:
        print (int(n*m/2)+1)



prinMinPoints(5,7)
prinMinPoints(3,8)