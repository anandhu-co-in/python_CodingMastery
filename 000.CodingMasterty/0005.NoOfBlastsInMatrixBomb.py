# https://www.geeksforgeeks.org/amazon-interview-experience-sde-1-amazon-wow-2020/?ref=leftbar-rightbar
# 2. Given a matrix and there will be bombs in the cells, find the number of blasts. A group of connected bombs leads to blast.

# I fell in love with this problem!! A beautiful program showing the cuteness of recursion!!


def countBlasts(matrix,m,n):

    blasts=0

    for i in range(m):
        for j in range(n):

            def fire(i,j):
                if i>=m or i<0 or j>=n or j<0 or matrix[i][j]==0: return 0
                elif(matrix[i][j]==1):
                    matrix[i][j]=0
                    return  1+fire(i,j+1)+fire(i,j-1)+fire(i-1,j)+fire(i+1,j)+fire(i+1,j+1)+fire(i-1,j-1)+fire(i+1,j-1)+fire(i-1,j+1)  #Remove unwanted ones based on how bombs connected
            if fire(i,j)>2:
                blasts=blasts+1

    print("No of Blasts is --> {}".format(blasts))


matrix=([1,0,1,1,0],
        [1,0,0,0,0],
        [1,1,1,1,1],
        [1,1,0,1,0],
        [1,0,0,1,1])

countBlasts(matrix,5,5)