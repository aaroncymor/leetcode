class Node:
    def __init__(self, name):
        self.children = []
        self.name = name
    
    def addChild(self, name):
        self.children.append(Node(node))
        return self
    
    def depthFirstSearch(self, array):
        pass


if __name__ == "__main__":
    a = Node("A")
    a.depthFirstSearch([])
    