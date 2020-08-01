from math import floor

class node:
    def __init__(self,v,p):
        self.value=v
        self.priority=p

class PriorityQueue:

    def __init__(self):
        self.values=[]

    def enqueue(self,val,prio):
        newNode=node(val,prio)
        self.values.append(newNode)
        self.bubbleUp()
        print("Inserted {} with priority {}".format(val,prio))

    def bubbleUp(self):
        i=len(self.values) -1
        current=self.values[i]
        while(i>0):
            parentI=floor((i-1)/2)
            parent=self.values[parentI]
            if parent.priority<=current.priority :break
            self.values[parentI]=current
            self.values[i]=parent
            i=parentI


    def dequeue(self):

        if len(self.values)==0:
            print("Heap Empty. No max value present")
        else:
            print("Max Value Extracted {}".format(self.values[0].value))
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

            if(child1Id<length and self.values[child1Id].priority<=self.values[parentId].priority):
                swap=child1Id

            if(swap!=None and child2Id<length and self.values[child2Id].priority<=self.values[swap].priority) or (swap==None  and child2Id<length and self.values[child2Id].priority<=self.values[parentId].priority):
                swap=child2Id

            if swap!=None :
                # print("Swapping {}  and {}".format(self.values[parentId], self.values[swap]))
                self.values[swap],self.values[parentId]=self.values[parentId],self.values[swap]
                parentId=swap

            else :
                break


myPriorityQueue=PriorityQueue()

myPriorityQueue.enqueue("Flue",3)
myPriorityQueue.enqueue("Fever",1)
myPriorityQueue.enqueue("Corona",2)
myPriorityQueue.enqueue("Accident",4)
myPriorityQueue.enqueue("Accident2",4)


myPriorityQueue.dequeue()
myPriorityQueue.dequeue()
myPriorityQueue.dequeue()
myPriorityQueue.dequeue()
myPriorityQueue.dequeue()
myPriorityQueue.dequeue()



myPriorityQueue.enqueue("prio0",0)
myPriorityQueue.enqueue("prio1",1)
myPriorityQueue.enqueue("prio2",2)
myPriorityQueue.enqueue("prop5",5)
myPriorityQueue.enqueue("prop0dupli",0)
myPriorityQueue.dequeue()
myPriorityQueue.dequeue()
myPriorityQueue.dequeue()
myPriorityQueue.dequeue()
myPriorityQueue.dequeue()