# https://leetcode.com/problems/merge-two-sorted-lists/

# This wont work, already have leetcode already has setup to execute with the linked lists nodess chummaa etc

#
# def mergeTwoLists(self, l1, l2):
#     result = ListNode()
#     dummy = result
#
#     while l1 and l2:
#
#         if (l1.val < l2.val):
#             result.next = l1
#             l1 = l1.next
#         else:
#             result.next = l2
#             l2 = l2.next
#
#         result = result.next
#
#     result.next = l1 or l2
#
#     return dummy.next


# Optimal Solution Using Kadanes Algorithm :
def findMaxSubArrayKadanes(array):

    size = len(array)
    result=array[0]
    currentMax = array[0]
    for i in range(1, size):
        currentMax=max(array[i],currentMax+array[i])
        result=max(currentMax,result)

    print("\nMaximum sum using Kadanes Algorithm --> {}".format(result))

# array = [-2, -3, 4, -1, -2, 1, 5, -3]
findMaxSubArrayKadanes([])