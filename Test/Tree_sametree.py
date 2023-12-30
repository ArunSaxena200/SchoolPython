class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def isSameTree(self, p, q):
        '''
        len is same
        ist node is same
        2 sets are same 

        '''
        if not p and not q:
            return True
        if not p or not q:
            return False
            
        return(p.val==q.val and Solution.isSameTree(p.left,q.left) and Solution.isSameTree(p.right,q.right))

# Example usage:
# Construct two binary trees
# Tree 1:
#    1
#   / \
#  2   3
tree1 = TreeNode(1, TreeNode(2), TreeNode(3))

# Tree 2:
#    1A
#   / \
#  2   3
tree2 = TreeNode(1, TreeNode(2), TreeNode(3))

# Check if the trees are the sameA
result = TreeNode.isSameTree(tree1, tree2)
print(result)  # Output: True
