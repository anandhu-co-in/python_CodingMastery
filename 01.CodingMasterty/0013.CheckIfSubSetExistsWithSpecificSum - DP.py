#Given an array, find if there is a sub array with specific sum - using DP!

# 5 2 3 4  , 8

#       0 1 2 3 4 5 6 7 8
# 0   5 t f f f f t f f f
# 1   2 t f t f f t f t f
# 2   3 t f t t
# 3   4 t


def show(matrix):
    for i in matrix:
        print(i)


def hassubArrayWithSum(array, sum):

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
    return matrix[len(array)-1][sum]


array=[3,2,8,5,1,2,3,4,5,6]
print(hassubArrayWithSum(array,40))
print(hassubArrayWithSum(array,20))

array=[37, 43, 7, 54]
print(hassubArrayWithSum(array,54))

