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
hot = TreeNode("Hot")
cold = TreeNode("Cold")
newBT.leftchild = hot
newBT.rightchild = cold

"""
- Root Node
    - Left Subtree
        - Right Subtree
"""
def preorderTraversal(rootNode):
    if not rootNode:
        return
    print(rootNode.data)
    preorderTraversal(rootNode.leftchild)
    preorderTraversal(rootNode.rightchild)

"""
INORDER TRAVERSAL
- Left Subtree
    - Root Node 
        - Right Subtree
"""

def inorderTraversal(rootNode):
    if not rootNode:
        return
    inorderTraversal(rootNode.leftchild)
    print(rootNode.data)
    inorderTraversal(rootNode.rightchild)

"""
POSTORDER TRAVERSAL
- Left Subtree
    - Right Subtree
        - Root Node 
"""
def postOrderTraversal(rootNode):
    if not rootNode:
        return
    postOrderTraversal(rootNode.leftchild)
    postOrderTraversal(rootNode.rightchild)
    print(rootNode.data)

"""
Level Order Traversal
"""

print("Preorder")
preorderTraversal(newBT)

print("Inorder")
inorderTraversal(newBT)

print("PostOrder")
postOrderTraversal(newBT)