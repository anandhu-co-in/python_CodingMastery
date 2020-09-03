#Given a sorted array , find the pair that gives sum zero
#Source Udemy section 5

array=[-3,-1,2,3]


def findzerosumPair():

    pointer1=0;
    pointer2=len(array)-1

    while pointer1 != pointer2 :

        if array[pointer1]+array[pointer2] == 0:
            return([array[pointer1],array[pointer2]])

        elif array[pointer1]+array[pointer2] > 0:
            pointer2=pointer2-1
        else:
            pointer1=pointer1+1

    return False



print(findzerosumPair())
