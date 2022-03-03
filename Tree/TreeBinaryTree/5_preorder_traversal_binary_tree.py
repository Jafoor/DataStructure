"""
Traversal of Binary Tree

Depth first search
- Preorder traversal
- Inorder traversal
- Post oder traversal

Breadth first search
- Level order traversal
"""

class TreeNode:
    def __init__(self, data) -> None:
        self.data = data
        self.leftchild = None
        self.rightchild = None

newBT = TreeNode("Drink")
leftchild = TreeNode("Hot")
rightchild = TreeNode("Cold")
newBT.leftchild = leftchild
newBT.rightchild = rightchild

def preorderTraversal(rootNode):
    if not rootNode:
        return
    print(rootNode.data)
    preorderTraversal(rootNode.leftchild)
    preorderTraversal(rootNode.rightchild)

preorderTraversal(newBT)