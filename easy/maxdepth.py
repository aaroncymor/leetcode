class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def maxDepth(root):

    if not isinstance(root, TreeNode):
        raise ValueError("not treenode object")
    
    if root == None:
        return 0
    
    if root.left == None and root.right == None:
        return 1
    else:
        #print(root.left.val)
        left = maxDepth(root.left)
        #print(root.right.val)
        right = maxDepth(root.right)
        return 1 + max(left, right)



if __name__ == "__main__":
    root = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
    print(maxDepth(root))