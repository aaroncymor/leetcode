def findClosestValueInBst(tree, target):
    # Python list can store and change value even outside
    # of the recursive function
    closest = [tree.value]
    distance = abs(tree.value - target)
    bstHelper(tree, target, distance, closest)
    return closest[0]

def bstHelper(node, target, distance, closest):
    if not node:
        return
    
    # leaf node. Go one up node to get left and right child values
    if not node.left and not node.right:
        return
    
    leftVal = node.left.value if node.left else 0
    rightVal = node.right.value if node.right else 0

    leftDistance = 0
    # tree validity: left value < parent value
    if leftVal and (leftVal < node.value):
        leftDistance = abs(target - leftVal)

        # if leftDistance is lower than current distance we have
        # We assign new value as leftDistance and our current closest
        # node to target will be the node.left.value
        if leftDistance < distance:
            distance = leftDistance
            closest[0] = leftVal

    rightDistance = 0
    # tree validity: right value > parent value
    if rightVal and (rightVal > node.value):
        rightDistance = abs(target - rightVal)

        # if rightDistance is lower than current distance we have
        # We assign new value as rightDistance and our current closest
        # node to target will be the node.right.value
        if rightDistance < distance:
            distance = rightDistance
            closest[0] = rightVal

    bstHelper(node.left, target, distance, closest)
    bstHelper(node.right, target, distance, closest)
    

class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


if __name__ == "__main__":
    root = BinaryTree(10)
    a = BinaryTree(5)
    b = BinaryTree(15)
    c = BinaryTree(2)
    d = BinaryTree(5)
    e = BinaryTree(1)
    f = BinaryTree(13)
    g = BinaryTree(22)
    h = BinaryTree(14)

    # 5 <- 10 -> 15
    root.left = a
    root.right = b

    # 2 <- 5 -> 5
    a.left = c
    a.right = d

    # 1 <- 2
    c.left = e

    # 13 <- 15 -> 22
    b.left = f
    b.right = g

    # 13 -> 14
    f.right = h

    print(findClosestValueInBst(root, 14))
