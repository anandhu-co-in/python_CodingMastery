class node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root=None

    def insert(self,value):

        newNode=node(value)

        if(self.root==None):
            self.root=newNode
            print("Set {} root node".format(value))
        else:
            current=self.root
            while True:
                if current.val==value:
                    print("Not able to insert. Same value already present!")
                    return
                elif(value<current.val):
                    if current.left==None:
                        current.left=newNode
                        print("Inserted {}".format(value))
                        return
                    else:
                        current=current.left
                else:
                     if(current.right==None):
                        current.right=newNode
                        print("Inserted {}".format(value))
                        return
                     else:
                        current=current.right

    def find(self,value):
        if self.root==None:
            print("Not found. Tree empty")
        else:
            current=self.root
            found=False
            while found==False and current!=None:
                if current.val>value:
                    current=current.left
                elif current.val<value:
                    current=current.right
                else:
                    found=True
            if found==True:
                print("Found {}".format(value))
            else:
                print("Value {} is not found in the Tree".format(value))

    def BFS(self):
        current=self.root
        queue=[]
        result=[]
        queue.append(current)
        while(len(queue)!=0):
            current=queue.pop(0)
            result.append(current.val)
            if(current.left!=None):
                queue.append(current.left)
            if(current.right!=None):
                queue.append(current.right)
        print("BFS Traversal is {} ".format(result))

    def DFSPreorder(self):
        result=[]
        def traverse(node):
            result.append(node.val)
            if(node.left!=None):traverse(node.left)
            if(node.right!=None):traverse(node.right)

        traverse(self.root)
        print("DFS Preorder Traversal is {} ".format(result))

    def DFSPostOrder(self):
        result=[]
        def traverse(node):
            result.append(node.val)
            if(node.right!=None):traverse(node.right)
            if (node.left != None): traverse(node.left)

        traverse(self.root)
        print("DFS Postorder Traversal is {} ".format(result))


    def DFSInorder(self):
        result=[]
        def traverse(node):

            if (node.left != None): traverse(node.left)
            result.append(node.val)
            if (node.right != None): traverse(node.right)


        traverse(self.root)
        print("DFS Inorder Traversal is {} ".format(result))




#Time Complexity O(lognN) for insert find



myBST=BinarySearchTree()
myBST.insert(10)
myBST.insert(20)
myBST.insert(30)
myBST.insert(10)
myBST.insert(40)
myBST.insert(50)
myBST.insert(40)
myBST.insert(400)
myBST.insert(140)
myBST.insert(440)
myBST.insert(480)
myBST.insert(440)
myBST.find(440)


myBST2=BinarySearchTree()
myBST2.insert(8)
myBST2.insert(3)
myBST2.insert(10)
myBST2.insert(14)
myBST2.insert(13)
myBST2.insert(6)
myBST2.insert(1)
myBST2.insert(7)
myBST2.insert(4)
myBST2.BFS()
myBST2.DFSPreorder()
myBST2.DFSPostOrder()
myBST2.DFSInorder()




