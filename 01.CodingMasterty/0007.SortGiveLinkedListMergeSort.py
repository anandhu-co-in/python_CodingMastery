# https://www.geeksforgeeks.org/amazon-interview-experience-sde-1-amazon-wow-2020/?ref=leftbar-rightbar
# 1. Sort the given linked list.


def show(list):
    if list.head==None:
        print("EmptyList")
    else:
        result=[]
        current = list.head
        while current != None:
            result.append(current.val)
            current = current.next
        #print(result)
        return result


class node:
    def __init__(self,val):
        self.val=val
        self.next=None

class LinkedList:
    def __init__(self):
        self.head=None
        self.tail=None



    def push(self,value):
        newNode=node(value)
        if self.head==None:
            self.head=self.tail=newNode

        else:
            self.tail.next=newNode
            self.tail=newNode

def merge(list1,list2):

    print("Merging LinkedLists {} and {} to --> ".format(show(list1),show(list2)), end=" ")

    if list1.head==None:
        return list2
    if list2.head==None:
        return list1

    mergedList=LinkedList()

    first=list1.head
    second=list2.head

    if first.val<=second.val:
        temp=first
        first=first.next
    else:
        temp=second
        second=second.next

    mergedList.head=temp

    while(first!=None and second!=None):

        if first.val<=second.val:
            temp.next=first
            temp=first
            first=first.next
        else:
            temp.next=second
            temp=second
            second=second.next


    if first==None : temp.next=second
    if second==None: temp.next=first

    while(temp.next!=None):
        temp=temp.next

    mergedList.tail=temp

    print(show(mergedList))

    return mergedList



def mergeSortLL(list):
    if (list.head==None or (list.head==list.tail)) :
        return list
    else:
        first=list.head
        second=list.head

        while(second.next !=None and second.next.next!=None):
            second=second.next.next
            first=first.next

        if second.next!=None:
            second=second.next

        firsthalf=LinkedList()
        secondHalf=LinkedList()

        firsthalf.head=list.head
        firsthalf.tail=first
        secondHalf.head=first.next
        secondHalf.tail=list.tail

        first.next = None

        return merge (mergeSortLL(firsthalf),mergeSortLL(secondHalf))


myLinkedList=LinkedList()
myLinkedList.push(7)
myLinkedList.push(20)
myLinkedList.push(15)
myLinkedList.push(30)
myLinkedList.push(1)
myLinkedList.push(2)
myLinkedList.push(4)
myLinkedList.push(5)
myLinkedList.push(6)
myLinkedList.push(3)

print("\nOriginal Linked List --> {}\n".format(show(myLinkedList)))

sortedList=mergeSortLL(myLinkedList)

print("\nSorted Linked List --> {}\n".format(show(sortedList)))
