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

def postOrderTraversal(root):
    if root is None:
        return

    btData = []

    postOrderTraversal(root.left)
    postOrderTraversal(root.right)
    btData.append(root.data)

    print(btData)

def preOrderTraversal(root):
    if root is None:
        return
    
    btData = []
    btData.append(root.data)
    preOrderTraversal(root.left)
    preOrderTraversal(root.right)

    print(btData)

def inOrderTraversal(root):
    if root is None:
        return
    
    btData = []
    inOrderTraversal(root.left)
    btData.append(root.data)
    inOrderTraversal(root.right)

    print(btData)

postOrderTraversal(root)

print()
print()

preOrderTraversal(root)

print()
print()

inOrderTraversal(root)