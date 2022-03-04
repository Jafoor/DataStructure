"""
Create Binary Tree Using Linked List
- Creation of Tree
- Insertion of a node
- Deletion of a node
- Search for a value
- Traverse all nodes
- Deletion of tree
"""

class TreeNode:
    def __init__(self, data) -> None:
        self.data = data
        self.leftChild = None
        self.rightChild = None


newBT = TreeNode("Drinks") # Time Complexity O(1) Space Complexity O(1)