# Bottom View of a Binary Tree https://www.geeksforgeeks.org/bottom-view-binary-tree/
# Given a Binary Tree, we need to print the bottom view from left to right. A node x is there in output if x is the bottommost node at its horizontal distance. Horizontal distance of left child of a node x is
# equal to horizontal distance of x minus 1, and that of right child is horizontal distance of x plus 1.
#
# Examples:
#                       20
#                     /    \
#                   8       22
#                 /   \      \
#               5      3      25
#                     / \
#                   10    14
#
# For the above tree the output should be 5, 10, 3, 14, 25.
#
# If there are multiple bottom-most nodes for a horizontal distance from root, then print the later one in level traversal. For example, in the below diagram, 3 and 4 are both the bottom-most nodes at
# horizontal distance 0, we need to print 4.
#
#
#                       20
#                     /    \
#                   8       22
#                 /   \    /   \
#               5      3 4     25
#                     / \
#                   10    14

# For the above tree the output should be 5, 10, 4, 14, 25.

# it took me 4 hours to solve this!!! great work ;D ;D !!!
#But what all did I learn?? --> Horizondal distance, Dictionary sorting in python, Also realized that BFS is called Level Order Traversal



class node:
    def __init__(self,val):
        self.valu=val
        self.left=None
        self.right=None
        hd=None

class BTree:
    def __init__(self):
        self.root=None

    def levelOrderTraversal(self):
        horix={}
        current=self.root
        if current==None : return "Empty Tree"
        queue=[]
        queue.append([current,0])
        horix[0]=current.valu

        while(len(queue)!=0):
            item=queue.pop(0)
            level=item[1]
            if item[0].left !=None :
                queue.append([item[0].left,level-1])
                horix[level-1]=item[0].left.valu
            if item[0].right !=None :
                queue.append([item[0].right,level+1])
                horix[level+1] = item[0].right.valu

        result=[]
        for key in sorted(horix):
            result.append(horix[key])
        return result


BT2=BTree()
BT2.root=node(20)
BT2.root.left=node(8)
BT2.root.right=node(22)
BT2.root.left.left=node(5)
BT2.root.left.right=node(3)
BT2.root.left.right.left=node(10)
BT2.root.left.right.right=node(14)
BT2.root.right.right=node(25)
print(BT2.levelOrderTraversal())


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




