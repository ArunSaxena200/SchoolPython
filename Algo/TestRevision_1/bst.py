class BST:
    def __init__(self,value,left = None,right= None):
        self.value = value
        self.left = left
        self.right = right
    
    def insert(self,value):
        startNode = self
        while True:
            if value < startNode.value:
                if startNode.left is None:
                    startNode.left  = BST(value)
                    break
                else:
                    startNode = startNode.left
            else:
                if startNode.right is None:
                    startNode.right = BST(value)
                    break
                else:
                    startNode = startNode.right

bst1 = BST(10)
bst1.insert(5)
bst1.insert(12)
bst1.insert(11)
bst1.insert(15)
bst1.insert(16)
bst1.insert(8)
bst1.insert(7)


def walk(bst):
    if bst is not None:
        
        walk(bst.left)
        print(bst.value)
        walk(bst.right)
        

walk(bst1)
        