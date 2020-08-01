# https://www.geeksforgeeks.org/amazon-interview-experience-sde-1-amazon-wow-2020/?ref=leftbar-rightbar
# 3. Level order traversal of a tree.,


class node:
    def __init__(self,val):
        self.value=val
        self.left=None
        self.right=None


class BTree:
    def __init__(self):
        self.root=None

    def levelOrderTraversal(self):

        if self.root==None :
            return "Tree is empty"
        result=[]
        queue=[self.root]
        while len(queue)!=0:
            item=queue.pop(0)
            result.append(item.value)
            if item.left!=None : queue.append(item.left)
            if item.right!=None : queue.append(item.right)

        return result



#
#                       20
#                     /    \
#                   8       22
#                 /   \    /   \
#               5      3 4     25
#                     / \
#                   10    14




BT=BTree()

BT.root=node(20)
BT.root.left=node(8)
BT.root.right=node(22)
BT.root.left.left=node(5)
BT.root.left.right=node(3)
BT.root.right.left=node(4)
BT.root.right.right=node(25)
BT.root.left.right.left=node(10)
BT.root.left.right.right=node(14)
print(BT.levelOrderTraversal())