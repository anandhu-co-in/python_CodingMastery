#https://www.geeksforgeeks.org/find-number-of-islands/

# Find the number of islands | Set 1 (Using DFS)
# Given a boolean 2D matrix, find the number of islands. A group of connected 1s forms an island. For example, the below matrix contains 5 islands
#
# Example:
#
# Input : mat[][] = {{1, 1, 0, 0, 0},
#                    {0, 1, 0, 0, 1},
#                    {1, 0, 0, 1, 1},
#                    {0, 0, 0, 0, 0},
#                    {1, 0, 1, 0, 1}
# Output : 5
# This is a variation of the standard problem: “Counting the number of connected components in an undirected graph”.



#isnt this same as the bomb blast think i did earlier??




def countIslands(matrix):

    rows=len(matrix)
    cols=len(matrix[0])
    count=0

    for i in range(rows):
        for j in range(cols):

            def isIland(i,j):
                if (not 0<=i<rows) or (not 0<=j<cols) or (matrix[i][j]==0):
                    return 0
                else:
                    matrix[i][j]=0
                    return 1 + isIland(i+1,j) + isIland(i,j+1) + isIland(i,j-1) + isIland(i-1,j-1) + isIland(i+1,j+1) + isIland(i-1,j+1)+ isIland(i+1,j-1)

            if isIland(i,j)>0:
                count+=1
    print(count)


matrix=([1,0,1,1,0],
        [1,0,0,0,0],
        [1,1,0,0,1],
        [1,1,0,0,0],
        [1,0,0,1,1])

countIslands(matrix)






