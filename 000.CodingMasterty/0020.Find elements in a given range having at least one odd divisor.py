# # https://www.geeksforgeeks.org/find-elements-in-a-given-range-having-at-least-one-odd-divisor/

# Given two integers N and M, the task is to print all elements in the range [N, M] having at least one odd divisor.
#
# Examples:
#
# Input: N = 2, M = 10
# Output: 3 5 6 7 9 10
# Explanation:
# 3, 6 have an odd divisor 3
# 5, 10 have an odd divisor 5
# 7 have an odd divisor 7
# 9 have two odd divisors 3, 9
#
# Input: N = 15, M = 20
# Output: 15 17 18 19 20


#HAHAHA.. no no i know what u are thinking. STOP!!

# Any number which is a power of 2, does not have any odd divisors. THEORY:How to check if number is power of 2
# All other elements will have at least one odd divisors



def findNosWithOddDivisor(N,M):

    for x in range(N,M+1):
        if x>0 and x&(x-1)!=0 :   #<----- This is the equation using bitwise AND to check if x is Not Power of two x is power of 2 if x&(x-1) is 0
            print(x)

findNosWithOddDivisor(2,10)



