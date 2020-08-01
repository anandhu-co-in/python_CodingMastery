class Node:
    def __init__(self,val):
        self.val=val
        self.next=None
        self.prev=None


class DoublyLinkedList:


    def __init__(self):
        self.head=Node
        self.tail=None
        self.length=0

    def traverse(self):
        current=self.head
        while(current!=None):
            print(current.val,end= " ")
            current=current.next


    def push(self,val):
        newNode=Node(val)
        if self.length==0:
            self.head=newNode
            self.tail=newNode
        else:
            self.tail.next=newNode
            newNode.prev=self.tail
            self.tail=newNode

        self.length=self.length+1


    def pop(self):
        if self.length==0:
            return "LL Empty"

        poppedNode=self.tail

        if self.length==1:
            self.head=None
            self.tail=None
        else:
            self.tail=poppedNode.prev
            self.tail.next=None
            poppedNode.prev=None

        self.length=self.length-1
        return poppedNode.val


    def shift(self):

        if self.length == 0:
            return "LL Empty"

        poppedNode = self.head

        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.head = poppedNode.next
            self.head.prev=None
            poppedNode.next = None

        self.length = self.length - 1
        return poppedNode.val


    def unshift(self,val):
        newNode=Node(val)
        if self.length==0:
            self.head=newNode
            self.tail=newNode
        else:
            self.head.prev=newNode
            newNode.next=self.head
            self.head=newNode

        self.length=self.length+1


    def get(self,index):
        if(index<0 or index>=self.length) :
            return None
        else:
            count=0
            if index<self.length/2:
                current=self.head
                while count!=index :
                    current=current.next
                    count=count+1

            else:
                count=self.length-1
                current=self.tail
                while(count!=index):
                    current=current.prev
                    count=count-1

            return current

    def set(self,index,val):

        foundNode=self.get(index-1)
        if foundNode==None :
            print("Index not found for setting")
            return
        else:
            foundNode.val=val

    def insert(self,index,val):

        if index<0 or index>self.length :
            print("Insert failed")
            return
        if index==0 :
            self.unshift(val)
            return
        if index==self.length:
            self.push(val)
            return

        foundNode=self.get(index-1)
        if foundNode==None :
            print("Index not found for setting")
            return
        else:
            newNode=Node(val)
            newNode.prev=foundNode
            newNode.next=foundNode.next
            foundNode.next=newNode
            newNode.next.prev=newNode

        self.length=self.length+1



list = DoublyLinkedList()
list.push("Harry")
list.push("Ron")
list.push("Emma")
list.push("Chochang")
list.push("Ginny")
list.push("Penelop")
print("Popped {}".format(list.pop()))
print("Popped {}".format(list.pop()))
list.unshift("Dumbledore")
list.unshift("ProfSnape")
list.unshift("Lupin")
print("Shifted {}".format(list.shift()))
print("Value at position {} is {}".format(4,list.get(4).val))
list.set(4,"EmmaWatson")
list.insert(3,"Crush")
print("Value at position {} is {}".format(4,list.get(4).val))
list.insert(0,"Ceddrig")
list.insert(8,"Diggory")
list.traverse()
