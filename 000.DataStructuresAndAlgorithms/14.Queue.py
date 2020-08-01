class node:
    def __init__(self, val):
        self.val = val
        self.next = None

class queue:
    def __init__(self):
        self.size = 0
        self.first = None
        self.last = None

    def enqueue(self, val):

        newNode=node(val)

        if self.first==None:
            self.first=newNode
            self.last=newNode
        else:
            self.last.next=newNode
            self.last=newNode
        self.size=self.size+1


    def dequeue(self):

        if(self.first==None):
            print("Queue empty")
        else:
            temp=self.first
            if(self.first==self.last):
                self.last=None
            self.first=self.first.next
            self.size=self.size-1
            print(temp.val)
            return temp.val





myQueue=queue()

myQueue.enqueue(1)
myQueue.enqueue(2)
myQueue.enqueue(3)
myQueue.enqueue(4)
myQueue.dequeue()
myQueue.dequeue()
myQueue.dequeue()
myQueue.dequeue()
myQueue.dequeue()
myQueue.enqueue(4)
myQueue.dequeue()
myQueue.dequeue()
myQueue.dequeue()

#Big of of pupsh pop ot stack and enqueue and dequeue of queue is O(1)
#hover searching in sertion  will take O(n)






























