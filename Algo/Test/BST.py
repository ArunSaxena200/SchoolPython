class BST:
    def __init__(self,value,left = None,right = None):
        self.value = value
        self.left = left
        self.right = right
    
    def insert(self,value):
        startNode = self
        while True:
            if value < startNode.value:
                if startNode.left is None:
                    startNode.left = BST(value)
                    break
                else:
                    startNode = startNode.left
            else:
                if startNode.right is None:
                    startNode.right = BST(value)
                    break
                else:
                    startNode = startNode.right
    
    def contains(self,value):
        startNode = self
        while startNode is not None:
            if value<startNode.value:
                startNode = startNode.left
            elif value>startNode.value:
                startNode=startNode.right
            else: 
                return True
        return False



bst = BST(10)
bst.insert(5)
bst.insert(12)
bst.insert(11)
bst.insert(15)
bst.insert(16)
bst.insert(8)
bst.insert(7)
    

def walk(bst):
    if bst is not None:
        print(bst.value)
        walk(bst.left)
        walk(bst.right)


print(walk(bst))