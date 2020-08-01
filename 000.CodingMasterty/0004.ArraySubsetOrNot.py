# https://www.geeksforgeeks.org/amazon-interview-experience-sde-1-amazon-wow-2020/?ref=leftbar-rightbar
# 1. Given two arrays and we need to find whether one array is a subset of other or not
# Ex:
# array1: 1 6 5
# array2: 1 4 7 3 5 6
# o/p: yes



def checkIfArraySubstring(a1,a2):

    #For every element in small array
    for i in range(len(a2)):
        #ccompare with each element in large array
        for j in range(len(a1)):
            #if match is found break for!
            if a2[i]==a1[j] :
                break
            if j==len(a1)-1:return False

    return True

a1=[7,1,2,4,5,6,7,9]
a2=[9,6,5,7,8]

print(checkIfArraySubstring(a1,a2))


#I need to investigate if this has better solutions, say about other solutions using hash tables, etc