

def naiveSearch(string,key):

    counter=0
    for i in range(len(arr)-len(key)+1):
        for j in range(len(key)):
            if(string[i+j]!=key[j]):
                break
            if(j==len(key)-1):
                counter=counter+1

    print(counter)


arr="i love coins, I love miracles"
naiveSearch(arr, 'coins')
