def bubbleSort(arr):
    for i in range(len(arr),0,-1):   #Loop from length to 1, if 3 elements  3 to 1
        print(i)
        noswaps=True
        for j in range(0,i-1):  #Loop from First element to i-2, for first time this goes fom first element to last secong last, python range goes till one minus last tthats why jut i-1 not <i-1
            print("j " +str(j))
            if(arr[j]>arr[j+1]):
                arr[j],arr[j+1]=arr[j+1],arr[j]
                noswaps=False #to optimize, ie say no swaps in current iteration, it means alreay sorted everything. so no need to loop more! v r done!
        if(noswaps):
            print("noswapsin this iteration")
            break
    return arr

print(bubbleSort([7,5,4,6,2,9,3,7,3,5,7,0,1,2,3]))



#time complexity of bubble sort is O(n^2)  EN SQUAAAREEEE :-D