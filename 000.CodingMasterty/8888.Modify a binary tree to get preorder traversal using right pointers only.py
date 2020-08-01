#https://www.geeksforgeeks.org/modify-binary-tree-get-preorder-traversal-using-right-pointers/

# Modify a binary tree to get preorder traversal using right pointers only

# Given a binary tree.
# Modify it in such a way that after modification you can have a pre-order traversal of it using
# only the right pointers. uring modification, you can use right as well as left pointers.
#
# Examples:
#

# Input :    10
#           /   \
#         8      2
#       /  \
#     3     5

# Output :    10
#               \
#                8
#                 \
#                  3
#                   \
#                    5
#                     \
#                      2

# Explanation : The preorder traversal
# of given binary tree is 10 8 3 5 2.



class node:
    def __init__(self,v):
        self.value=v
        self.left=None
        self.right=None


class Tree:

    def __init__(self):
        self.root=None

    def preorderWithBothPointers(self):

        result=[]

        def traverse(node):
            result.append(node.value)
            if node.left!=None :
                traverse(node.left)
            if node.right!=None:
                traverse(node.right)
        traverse(self.root)

        print(result)

    def preorderWithRightPointerOnly(self):

        result=[]

        def traverse(node):
            result.append(node.value)
            if node.right!=None:
                traverse(node.right)
        traverse(self.root)

        print(result)


    def modifyTreeToRighPointerOnly(self):


        current=self.root
        while current is not None:
            if current.left is not None:
                temp=current.left
                current.left=None
                if current.right is not None:
                    import copy
                    temp2=copy.copy(temp)
                    while temp2.right is not None:
                        temp2=temp2.right
                    temp2.right=current.right
                current.right=temp
            current=current.right


# Input :    10
#             \
#               8
#
#           3      5
#                    \
#                     2


myTree=Tree()
myTree.root=node(10)
myTree.root.left=node(8)
myTree.root.left.left=node(3)
myTree.root.left.right=node(5)
myTree.root.right=node(2)

myTree.preorderWithBothPointers()
myTree.modifyTreeToRighPointerOnly()
myTree.preorderWithRightPointerOnly()






