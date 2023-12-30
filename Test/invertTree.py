def invertTree(self, root):
        if not root:
            return None
    
    # Swap left and right subtrees
        root.left, root.right = root.right, root.left
        self.invertTree(root.left)
        self.invertTree(root.right)
        # Recursively invert the left and right subtrees
        return root