#Merge Two Sorted Linked Lists In place:
#https://www.youtube.com/watch?v=KjLGthN30cg



class node:
    def __init__(self,val):
        self.value=val
        self.next=None

class linkedlist:
    def __init__(self):
        self.head=None
        self.tail=None

    def push(self,val):
        newNode=node(val)
        if self.head==None:
            self.head=self.tail=newNode
        else:
            self.tail.next=newNode
            self.tail=newNode

    def show(self,list):
        result = []
        current=list.head
        while(current!=None):
            result.append(current.value)
            current=current.next
        print(result)

    def merge(self,list1,list2):

        if list1.head==None :
            return list2
        if list2.head==None:
            return list1

        sortedList=linkedlist()

        first=list1.head
        second=list2.head

        if first.value<=second.value:
            temp=first
            first=first.next
        else:
            temp=second
            second=second.next

        sortedList.head=temp


        while(first!=None and second !=None):

            if first.value<=second.value :
                temp.next=first
                temp=first
                first=first.next
            else:
                temp.next=second
                temp=second
                second=second.next

        if first==None:
            temp.next=second
        if second==None:
            temp.next=first


        #I added below logic to get tail
        while temp.next!=None:
            temp=temp.next
        sortedList.tail=temp

        return sortedList



mylist1=linkedlist()
mylist1.push(10)
mylist1.push(20)
mylist1.push(30)
mylist1.push(40)


mylist2=linkedlist()
mylist2.push(5)
mylist2.push(15)
mylist2.push(25)
mylist2.push(35)
mylist2.push(45)
mylist2.push(55)
mylist2.push(65)

mylist1.show(mylist1)
mylist1.show(mylist2)

mylist3= mylist1.merge(mylist1,mylist2)
mylist1.show(mylist3)

print("Head of Merged List is {} and tails is {} ".format(mylist3.head.value,mylist3.tail.value))














