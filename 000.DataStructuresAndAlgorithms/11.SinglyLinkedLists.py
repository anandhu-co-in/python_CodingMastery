
class node:
    def __init__(self,val):
        self.val=val
        self.next=""

class singlyLinkedList:


    def __init__(self):
        self.head=""
        self.tail=""
        self.length=0

    def display(self):
        i=self.head
        print("")
        while(i!=""):
            print(i.val, end=" ")
            i=i.next
        print("  Length = "+str(self.length)+",",end=" ")

    def push(self,val):
        newNode=node(val)
        if(self.head==""):
            self.head=newNode
            self.tail=self.head
        else:
            self.tail.next=newNode
            self.tail=newNode
        self.length=self.length+1

    def pop(self):

        print("\nPoping from ", end="")
        self.display()

        if(self.head==""):
            print("\npop failed. LL empty")
        else:
            current=self.head
            newTail=current
            while(current.next!=""):
                newTail=current
                current=current.next
            self.tail=newTail
            self.tail.next=""
            self.length=self.length-1
            if(self.length==0):
                self.head=""
                self.tail=""

        print("\nAfter popping ", end="")
        self.display()

    def shift(self):

        print("\nshifting from ", end="")
        self.display()

        if(self.head==""):
            print("\nShift failed. LL empty ")
        else:
            self.head=self.head.next
            self.length=self.length-1
            if(self.length==0):
                self.tail=""


        print("\nAfter shifting ", end="")
        self.display()

    def unshift(self,val):

        print("\nb4 unshifting ", end=" ")
        self.display()

        newNode = node(val)

        if(self.head==""):
            self.head=newNode
            self.tail=newNode
        else:
            newNode.next=self.head
            self.head=newNode
        self.length=self.length+1

        print("\nAfter unshifting ", end="")
        self.display()

    def get(self,index):
        if(index<0 or index>=self.length):
            print("Get failed wrong index")
            return None
        else:
            counter=0
            current=self.head
            while(counter<index):
                current=current.next
                counter=counter+1

            print("\nValue at index {} is {} ".format(index,current.val))
            return current

    def set(self,index,val):
        fountNode=self.get(index)
        if(fountNode==None):
            print("set at index {} failed, index not found".format(index))
        else:
            fountNode.val=val

    def insert(self,index,value):
        if(index<0 or index>self.length):
            print("insert failed Wrong index {}".format(index))
        elif(index==0):
            self.unshift(value)
        elif(index==self.length):
            self.push(value)
        else:
            newNode=node(value)
            prev=self.get(index-1)
            temp=prev.next
            prev.next=newNode
            newNode.next=temp
            return

    def remove(self,index):
        if(index<0 or index>=self.length):
            print("Index {} not present for deletion".format(index))
        elif(index==0):
            self.shift()
        elif(index==self.length-1):
            self.pop()
        else:
            prev=self.get(index-1)
            prev.next=prev.next.next
            self.length=self.length-1

    #This is horrible : Maybe just biheat??!!
    def reverse(self):
        node=self.head
        self.head,self.tail=self.tail,self.head
        prev=""
        while(node!=""):
            next=node.next #Backup
            node.next=prev
            prev=node
            node=next


mylist=singlyLinkedList()

mylist.push(0)
mylist.push(1)
mylist.push(2)
mylist.push(3)
mylist.push(4)
mylist.push(5)

mylist.insert(4,7)
mylist.pop()
mylist.shift()
mylist.remove(0)
mylist.insert(2,8)
mylist.set(1,7)

mylist.display()
mylist.reverse()
mylist.push(51)
mylist.display()
mylist.reverse()
mylist.display()

#Expected answer 5127874



