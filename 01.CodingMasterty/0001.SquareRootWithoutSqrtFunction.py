#Problem - Print square root of a number without using sqrt function
import math


def recSearch(n,start,end):
    mid = (start + end) / 2
    print("New mid ={}".format(mid))

    if end-start<.000001 : return mid
    elif mid*mid<n: return recSearch(n,mid,end)
    else:return recSearch(n,start,mid)


def findSquareRoot(n):

    i=0
    while(i*i<=n):
        i=i+1
    i=i-1

    if(i*i==n):
        return i
    else:
        return round(recSearch(n,i,i+1),5)

        # start=i
        # end=i+1
        #
        # while(end-start>0.000001):
        #     print("Start = {} End = {} ".format(start, end))
        #     mid=(start+end)/2
        #     if mid*mid<n :
        #         start=mid
        #     else:
        #         end=mid
        #
        # return round(mid,5)

n=2.5

print("Calculated sqroot  = {}".format(findSquareRoot(n)))
print("Actual Square Root = {}".format(math.sqrt(n)))

