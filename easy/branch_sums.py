class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def branchSums(root):
    sums = []
    calculateBranchSums(root, 0, sums)
    return sums

def calculateBranchSums(node, runningSum, sums):
    if node is None:
        return
    
    newRunningSum = runningSum + node.value
    if node.left is None and node.right is None:
        sums.append(newRunningSum)
        return

    calculateBranchSums(node.left, newRunningSum, sums)
    calculateBranchSums(node.right, newRunningSum, sums)


if __name__ == "__main__":
    root = BinaryTree(1)
    a = BinaryTree(2)
    b = BinaryTree(3)
    c = BinaryTree(4)
    d = BinaryTree(5)
    e = BinaryTree(6)
    f = BinaryTree(7)
    g = BinaryTree(8)
    h = BinaryTree(9)
    i = BinaryTree (10)

    # 1 branches 2 and 3
    root.left = a
    root.right = b

    # 2 branches 4 and 5
    a.left = c
    a.right = d

    # 4 branches 8 and 9
    c.left = g
    c.right = h

    # 3 branches 6 and 7
    b.left = e
    b.right = f

    # 5 branches 10
    d.left = i

    print(branchSums(root))