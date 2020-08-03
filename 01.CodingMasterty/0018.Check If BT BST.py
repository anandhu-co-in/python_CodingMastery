# A program to check if a binary tree is BST or not
# A binary search tree (BST) is a node based binary tree data structure which has the following properties.
# • The left subtree of a node contains only nodes with keys less than the node’s key.
# • The right subtree of a node contains only nodes with keys greater than the node’s key.
# • Both the left and right subtrees must also be binary search trees.
#
# From the above properties it naturally follows that:
# • Each node (item in the tree) has a distinct key.


#https://www.geeksforgeeks.org/a-program-to-check-if-a-binary-tree-is-bst-or-not/




class node:
    def __init__(self,value):
        self.key=value
        self.left=None
        self.right=None

class Tree:
    def __init__(self):
        self.root=None



#MY DIRTY SOLUTION. MORE CUTE SOLUTION IS AT THE END
def isBST(root,dir=None,gp=None):


    if (root.left!=None and root.left.key>=root.key) :
        return False
    if (root.right!=None and root.key>=root.right.key):
        return False

    #If root node is left child of parent, then its right child should be less than grandparent
    if dir==0 and root.right!=None and root.right.key>=gp.key:
        return False

    #Also if root node is right of parent, then its left child whould be greater than parent
    if dir==1 and root.left!=None and root.left.key<=gp.key:
        return False

    if (root.left!=None and isBST(root.left,0,root)==False)  or (root.right!=None and isBST(root.right,1,root)==False):
        return False
    return True


myTree=Tree()
myTree.root=node(12)
myTree.root.left=node(5)
myTree.root.left.left=node(2)
myTree.root.left.right=node(11)
myTree.root.right=node(15)
myTree.root.right.left=node(13)
myTree.root.right.right=node(16)


print(isBST(myTree.root))






#LOOK HOW ELEGANET THE BELOW SOLUTION IS!!
min=-100
max=100

def isTreeBST(root,min,max):

    if root==None:
        return True
    elif(root.key<min or root.key>max):
        return False
    else: return(isBST(root.left,min,root.key-1) or isBST(root.right,root.key+1,max))


print(isBST(myTree.root))



















