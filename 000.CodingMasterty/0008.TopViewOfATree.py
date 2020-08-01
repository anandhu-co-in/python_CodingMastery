# https://www.geeksforgeeks.org/amazon-interview-experience-sde-1-amazon-wow-2020/?ref=leftbar-rightbar
# 2. Top view of a tree.


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
        horis={}
        queue=[[self.root,0]]


        while len(queue)!=0:
            item=queue.pop(0)

            if item[0].left!=None :
                queue.append([item[0].left,item[1]-1])
                if item[1]-1 not in horis:
                    horis[item[1]-1]=item[0].left.value
            if item[0].right!=None :
                queue.append([item[0].right,item[1]+1])
                if item[1]+1 not in horis:
                    horis[item[1]+1]=item[0].right.value


        result=[]
        for i in sorted(horis):
            result.append(horis[i])
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