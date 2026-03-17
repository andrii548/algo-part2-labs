class BinaryTree:
    def __init__(self, value, left=None, right=None, parent=None):
        self.value = value
        self.left = left
        self.right = right
        self.parent = parent
        
    def find_successor(node):
        if not node:
            return None
        current = None

        if node.right:
            current = node.right
            while current.left:
                current = current.left
            successor = current
        else:
            current = node
            parent = node.parent
            while parent is not None and current == parent.right:
                current = parent
                parent = parent.parent
            successor = parent

        return successor