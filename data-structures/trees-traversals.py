"""Below code is the implementation of Tree Traversals - Inorder, preorder and postorder"""

class TreeNode:
    def __init__(self, val, left = None, right = None):
        self.val = val
        self.left = None
        self.right = None
    def inorder_traversal(self, root):
        final = []
        def helper(node):
            if node is not None:
              helper(node.left)
              final.append(node.val)
              helper(node.right)
        helper(root)
        return final
    
    def preorder_traversal(self, root):
        final = []
        def helper(node):
            if node is not None:
              final.append(node.val)
              helper(node.left)
              helper(node.right)
        helper(root)
        return final
    
    def postorder_traversal(self, root):
        final = []
        def helper(node):
            if node is not None:
              helper(node.left)
              helper(node.right)
              final.append(node.val)
        helper(root)
        return final

#     1
#    / \
#   2   3
#  / \   \
# 4   5   6  

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.right = TreeNode(6)

print("Inorder: ",root.inorder_traversal(root))  # [4, 2, 5, 1, 3, 6]
print("Preorder: ",root.preorder_traversal(root)) # [1, 2, 4, 5, 3, 6]
print("Postorder: ",root.postorder_traversal(root)) # [4, 5, 2, 6, 3, 1]
