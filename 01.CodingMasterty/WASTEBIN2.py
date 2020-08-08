# aPI = "3141592653 58979323846263383279"
#
# bIN = ['314', '49', '9001', '15926535897', '14', '9323','846263383279', '4', '793']
#
# PI = "314159265358979323846263383279"
#
# IN = ['314', '49', '9001', '15926535897', '14', '9323','846263383279', '4', '793']
#
#
# def findMatch(a, b):
#     index = []
#     pos_a = 0
#     count_match = 0
#
#     for i in range(0, len(b)):
#         if pos_a >= len(a):
#             break
#         if checkStr(a, pos_a, b, i) == True:
#             pos_a += len(b[i])
#             count_match += 1
#             index.append(b[i])
#         else:
#             pos_a = pos_a
#     return f"{count_match - 1}({' '.join(index)})"
#
#
# def checkStr(strA, pos_a, listB, pos_b):
#     for i in range(0, len(listB[pos_b])):
#         if strA[pos_a + i] != listB[pos_b][i]:
#             return False
#         else:
#             return True
#
#
# print(findMatch(PI, IN))



PI = "314159265358979323846263383279"

print(PI[0:1])















