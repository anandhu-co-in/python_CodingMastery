#Find the largest sub array with minium distance 4


l=[4,16,5,3,3,1]
maximum=0
for i in l:
    c=l.count(i)
    d=l.count(i-1) #//onnu kuravlla no enname
    c=c+d
    if c > maximum:
        maximum=c
print(maximum)