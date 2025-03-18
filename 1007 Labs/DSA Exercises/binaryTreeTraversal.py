class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

# Constructing a simple binary tree
root = TreeNode(4)
root.left = TreeNode(2)
root.right = TreeNode(6)
root.left.left = TreeNode(1)
root.left.right = TreeNode(3)
root.right.left = TreeNode(5)
root.right.right = TreeNode(7)

def postOrderTraversal(root, btData):
    if root is None:
        return
    postOrderTraversal(root.left, btData)
    postOrderTraversal(root.right, btData)
    btData.append(root.data)

def preOrderTraversal(root, btData):
    if root is None:
        return
    btData.append(root.data)
    preOrderTraversal(root.left, btData)
    preOrderTraversal(root.right, btData)

def inOrderTraversal(root, btData):
    if root is None:
        return
    inOrderTraversal(root.left, btData)
    btData.append(root.data)
    inOrderTraversal(root.right, btData)

# Initialize an empty list for each traversal
postOrderData = []
preOrderData = []
inOrderData = []

# Perform the traversals
postOrderTraversal(root, postOrderData)
preOrderTraversal(root, preOrderData)
inOrderTraversal(root, inOrderData)

# Debugging step: Print intermediate results to see if data is being appended
print("Post-order Traversal:", postOrderData)  # Should print: [1, 3, 2, 5, 7, 6, 4]
print("Pre-order Traversal:", preOrderData)    # Should print: [4, 2, 1, 3, 6, 5, 7]
print("In-order Traversal:", inOrderData)      # Should print: [1, 2, 3, 4, 5, 6, 7]