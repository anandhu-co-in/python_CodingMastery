class node:
    def __init__(self, val):
        self.val = val
        self.next = ""


class stack:
    def __init__(self):
        self.size = 0
        self.first = None
        self.last = None

    def push(self, val):
        newNode = node(val)
        if self.first == None:
            self.first = newNode
            self.last = newNode
        else:
            temp = self.first
            self.first = newNode
            newNode.next = temp

        self.size=self.size+1
        return self.size


    def pop(self):

        if self.first==None:
            print("Empty")
            return None
        else:
            temp=self.first
            if(self.first==self.last):
                self.first=self.last=None
            else:
                self.first=self.first.next

            self.size=self.size-1
            print(temp.val)
            return temp.val



myStack=stack()

myStack.pop
myStack.push(1)
myStack.push(2)
myStack.push(3)
myStack.pop()
myStack.pop()
myStack.pop()
myStack.pop()
myStack.push(1)
myStack.push(2)
print(myStack.size)
myStack.push(3)
print(myStack.size)
myStack.pop()
myStack.pop()
myStack.pop()
myStack.pop()










