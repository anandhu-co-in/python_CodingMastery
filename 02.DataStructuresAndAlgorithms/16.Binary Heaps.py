from math import floor


class BinaryHeap:

    def __init__(self):
        self.values=[]

    def insert(self,val):
        self.values.append(val)
        self.bubbleUp()
        print("Inserted {} ".format(val))


    def bubbleUp(self):
        i=len(self.values) -1
        current=self.values[i]
        while(i>0):
            parentI=floor((i-1)/2)
            parent=self.values[parentI]
            if parent>current :break
            self.values[parentI]=current
            self.values[i]=parent
            i=parentI


    def extractMax(self):

        if len(self.values)==0:
            print("Heap Empty. No max value present")
        else:
            print("Max Value Extracted {}".format(self.values[0]))
            lastval = self.values.pop()
            if len(self.values)>0 :
                self.values[0]=lastval
                self.syncDown()

    def syncDown(self):

        parentId=0
        length=len(self.values)

        while(True):

            child1Id=2*parentId+1
            child2Id=2*parentId+2

            swap=None

            if(child1Id<length and self.values[child1Id]>self.values[parentId]):
                swap=child1Id

            if(swap!=None and child2Id<length and self.values[child2Id]>self.values[swap]) or (swap==None  and child2Id<length and self.values[child2Id]>self.values[parentId]):
                swap=child2Id

            if swap!=None :
                # print("Swapping {}  and {}".format(self.values[parentId], self.values[swap]))
                self.values[swap],self.values[parentId]=self.values[parentId],self.values[swap]
                parentId=swap

            else :
                break


myheap=BinaryHeap()

myheap.insert(41)
myheap.insert(39)
myheap.insert(33)
myheap.insert(18)
myheap.insert(27)
myheap.insert(12)
myheap.insert(55)
myheap.insert(555)
myheap.insert(554)
myheap.insert(553)

print(myheap.values)

myheap.extractMax()
myheap.extractMax()
myheap.extractMax()
myheap.extractMax()
myheap.extractMax()
myheap.extractMax()
myheap.extractMax()
myheap.extractMax()
myheap.extractMax()
myheap.extractMax()
myheap.extractMax()
myheap.extractMax()





