# Python code to modify binary tree for
# traversal using only right pointer

class newNode():

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

# Function to modify tree
def modifytree(root):
    right = root.right
    rightMost = root

    if (root.left):
        rightMost = modifytree(root.left)
        root.right = root.left
        root.left = None

    if (not right):
        return rightMost

    rightMost.right = right
    rightMost = modifytree(right)
    return rightMost


# printing using right pointer only
def printpre(root):
    while root != None:
        print(root.data, end=" ")
        root = root.right

if __name__ == '__main__':
    """ Constructed binary tree is 
         10 
        / \ 
      8    2 
    / \ 
   3   5	 """
    root = newNode(10)
    root.left = newNode(8)
    root.right = newNode(2)
    root.left.left = newNode(3)
    root.left.right = newNode(5)

    modifytree(root)
    printpre(root)

# This code is contributed by SHUBHAMSINGH10 , I should implement this recursive login in my solution file

