#Recursive Approch

def finSubsetwithsum(array,v,n,sum):

    if sum==0:
        print(v)
        return True
    if n==0:
        return False
    if array[n-1]>sum:
        return finSubsetwithsum(array,v,n-1,sum)
    else:
        withoutLastElement=finSubsetwithsum(array,v,n-1,sum)
        v2=[]+v
        v2.append(array[n-1])
        withLastElement=finSubsetwithsum(array,v2,n-1,sum-array[n-1])
        return (withLastElement or withoutLastElement)

array = [1,3,7,2,1,2]
print(finSubsetwithsum(array,[],len(array),4))

#LOL---> that was Simple But Amazing Logic!! My Brain is about to explode!!

