# https://www.geeksforgeeks.org/modify-binary-tree-get-preorder-traversal-using-right-pointers/

# Modify a binary tree to get preorder traversal using right pointers only

# Given a binary tree.
# Modify it in such a way that after modification you can have a pre-order traversal of it using
# only the right pointers. using modification, you can use right as well as left pointers.
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
    def __init__(self, v):
        self.value = v
        self.left = None
        self.right = None


class Tree:

    # Initialize root as none, while creating tree
    def __init__(self):
        self.root = None

    # To perfom preorder Traversal
    def preorderWithBothPointers(self):

        result = []

        def traverse(node):
            result.append(node.value)
            if node.left != None:
                traverse(node.left)
            if node.right != None:
                traverse(node.right)

        traverse(self.root)

        print(result)

    # Perform preorder, but we only via right childs
    def preorderWithRightPointerOnly(self):

        result = []

        def traverse(node):
            result.append(node.value)
            if node.right != None:
                traverse(node.right)

        traverse(self.root)

        print(result)

    # Logic 1
    def modifyTreeToRighPointerOnly(self):

        current = self.root
        while current is not None:
            # If there is a left sub Tree
            if current.left is not None:
                temp = current.left
                current.left = None
                # Move to the rightmost end of left subtree using a temp variable
                if current.right is not None:
                    temp2 = temp
                    while temp2.right is not None:
                        temp2 = temp2.right
                    # Attach the right subtree to the rightmost end of left subtree
                    temp2.right = current.right
                # Now attach the detached left sub tree as the new right child
                current.right = temp
            current = current.right

    # Different Logic
    def modifyTreeToRighPointerOnly2(self):
        current = self.root
        while current is not None:
            # If there is a left subtree
            if current.left is not None:
                temp = current
                # Find the righmost of the current node using a temp
                while (temp.right is not None):
                    temp = temp.right
                # And attach the left subtree there!
                temp.right = current.left
                current.left = None
            current = current.right


    def modifyTreeToRighPointerOnlyRECURSIVE(self):

        # For every node, if there is left subtree:
            # remember the right subtree
            # Do transform it and get the rightmost end of it
            # Attach the righ sub tree to that rightmost end
            # And detach left subtree and attach as right subtree

        # If there is a right to the righmost :
            # modify that rightmost,right and get the rightmost

        def modify(root):
            temp=root.right
            righmost=root
            if root.left is None and root.right is None:
                return righmost
            else:
                if root.left:
                    righmost=modify(root.left)
                    root.right=root.left
                    root.left=None

                #If we don't have right subtree, we are done!
                if temp is None:
                    return righmost
                #Oherwise. we need to attach it to the rightmost and modify it also!
                else:
                    righmost.right=temp
                    return modify(temp)

        modify(self.root)



# Create the same tree given in question
myTree = Tree()
myTree.root = node(10)
myTree.root.left = node(8)
myTree.root.left.left = node(3)
myTree.root.left.right = node(5)
myTree.root.right = node(2)

myTree.preorderWithBothPointers()
# myTree.modifyTreeToRighPointerOnly()
# myTree.modifyTreeToRighPointerOnly2()
myTree.modifyTreeToRighPointerOnlyRECURSIVE()
myTree.preorderWithRightPointerOnly()
