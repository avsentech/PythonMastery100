# Code #94: Inorder Traversal of a Binary Tree
# Tier: Inermediate
# Goal: Traverse a binary tree in inorder (Left→ Root → Right)

# Recursive Python Code
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def inorder_recursive(root):
    if not root:
        return []
    return inorder_recursive(root.left) + [root.val] + inorder_recursive(root.right)

# Sample Tree

root = TreeNode(1, None, TreeNode(2, TreeNode(3)))
print("🌿 Inorder Recursive:", inorder_recursive(root))

# Concept Breakdown
"""
    Concept             Description
    ----------------------------
    Inorder Traversal   Left→Root→Right
    Recursion           Elegant but stack-heavy
    Iteration+Stack     Manual control over traversal
"""
# Great of interview prep, tree-based problems, and understanding call stacks.