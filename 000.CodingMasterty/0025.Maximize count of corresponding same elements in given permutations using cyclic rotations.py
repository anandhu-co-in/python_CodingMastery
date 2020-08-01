# #https://www.geeksforgeeks.org/maximize-count-of-corresponding-same-elements-in-given-permutations-using-cyclic-rotations/
# Given two permutations P1 and P2 of numbers from 1 to N, the task is to find the maximum count of corresponding same elements in the given permutations by
# performing a cyclic left or right shift on P1.
#
# Examples:
#
# Input: P1 = [5 4 3 2 1], P2 = [1 2 3 4 5]
# Output: 1
# Explanation:
# We have a matching pair at index 2 for element 3.
#
# Input: P1 = [1 3 5 2 4 6], P2 = [1 5 2 4 3 6]
# Output: 3
# Explanation:
# Cyclic shift of second permutation towards right would give 6 1 5 2 4 3 and we get a match of 5, 2, 4. Hence the answer is 3 matching pairs.


# The logic is , swe need to findout, the total no of elements that can bet matched through each each possible no of shits to one direction from current postition of one of th arrray


def findNoOfMatchingElementsThroughCyclicShirt(A, B):
    n = len(B)
    bPositions = {} # To store position of second array
    shifts = [0 for x in range(n)]  # Example : if shifts[3]=3, it means 3 elements are matched with 3 shifts of array1

    for i in range(n):
        bPositions[B[i]] = i

    for i in range(n):
        d = bPositions[A[i]] - i

        # There are 3 cases :
        # d is positive, meaning, this element if shifted to right that many times will match with the one in B
        # d is 0 meaning, already this element matches with the on in B
        # d<0 means the B element is to the left, so we need calculate the equivalent right shifts using N-abd(d)

        if d < 0:
            d = n - abs(d)

        shifts[d] += 1

    # Now just find out the shifts which yields maximum no of matches
    print(max(shifts))


P1 = [1, 3, 5, 2, 4, 6]
P2 = [1, 5, 2, 4, 3, 6]

findNoOfMatchingElementsThroughCyclicShirt(P1, P2)

P1 = [3, 4, 5, 2, 1]
P2 = [1, 3, 2, 4, 5]
findNoOfMatchingElementsThroughCyclicShirt(P1, P2)

# Output
# 3
# 2
