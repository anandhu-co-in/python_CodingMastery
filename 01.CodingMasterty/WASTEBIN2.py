# print([1,2,4]+[5,6,7]+123)
#
# a=[1,2,4]
# # b=[5,6]
# # print(a+b)
# #
# # print(a)
# #
# #
#
# for x in a:
#     print(x)
#     a=""

# buckets = {0: [], 1: [], 2: [], 3: [], 4: [], 5: [], 6: [], 7: [], 8: [], 9: []}
# print(buckets)
# buckets = dict.fromkeys([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], [])
# print(buckets)
#
import sys


class MinStack(object):

    def __init__(self):

        self.values = []
        self.mins = []
        """
        initialize your data structure here.
        """

    def push(self, val):

        if len(self.mins) == 0 or self.mins[-1] >= val:
            self.mins.append(val)

        self.values.append(val)

    def pop(self):

        if self.mins[-1] == self.values.pop():
            self.mins.pop()

        self.values.pop()

    def top(self):

        return self.values[-1]
        """
        :rtype: int
        """

    def getMin(self):

        return self.mins[-1]
        """
        :rtype: int
        """






class MinStack(object):

    def __init__(self):

        self.stack = []

    def push(self, val):

        self.stack.append((val, min(1,2))

    def pop(self):

        if self.stack:
            return self.stack.pop()[-1][0]

        return None

    def top(self):

        if self.stack:
            return self.stack[-1][0]

        return None

    def getMin(self):

        if self.stack:
            return self.stack[-1][1]

        return None


    sys.m