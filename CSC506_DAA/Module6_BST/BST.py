class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class Tree:
    def __init__(self, arr):
        self.root = self.build_tree(sorted(set(arr)))

    def build_tree(self, arr):
        if not arr:
            return None
        mid = len(arr) // 2
        root = Node(arr[mid])
        root.left = self.build_tree(arr[:mid])
        root.right = self.build_tree(arr[mid + 1:])
        return root

    def walk_inorder(self, node):
        if node:
            self.walk_inorder(node.left)
            print(node.data)
            self.walk_inorder(node.right)

    def insert(self, value):
        self.root = self._insert(self.root, value)

    def _insert(self, node, value):
        if not node:
            return Node(value)
        if value < node.data:
            node.left = self._insert(node.left, value)
        elif value > node.data:
            node.right = self._insert(node.right, value)
        return node

    def delete(self, value):
        self.root = self._delete(self.root, value)

    def _delete(self, node, value):
        if not node:
            return None
        if value < node.data:
            node.left = self._delete(node.left, value)
        elif value > node.data:
            node.right = self._delete(node.right, value)
        else:
            if not node.left:
                return node.right
            elif not node.right:
                return node.left
            else:
                min_right = self.find_min(node.right)
                node.data = min_right.data
                node.right = self._delete(node.right, min_right.data)
        return node

    def find_min(self, node):
        while node.left:
            node = node.left
        return node

# Example usage:
arr = [1, 7, 4, 23, 8, 9, 4, 3, 5, 7, 9, 67, 6345, 324]
tree = Tree(arr)
print("base tree")
tree.walk_inorder(tree.root)

print("root",tree.root.data)  # Display the root node of the balanced binary tree

tree.insert(6)  # Insert a new value
print(tree.root.data)  # Display the root node after insertion

print("insert 6")
tree.walk_inorder(tree.root)


tree.delete(5)  # Delete a value
print(tree.root.data)  # Display the root node after deletion

print("delete 5")
tree.walk_inorder(tree.root)

