class Node:
    def __init__(self, value, priority):
        self.value = value
        self.priority = priority
        self.left = None
        self.right = None
        self.height = 1


class AVLPriorityQueue:
    def __init__(self):
        self.root = None

    def insert(self, value, priority):

        def _insert(node):
            if not node:
                return Node(value, priority)

            if priority >= node.priority:
                node.left = _insert(node.left)
            else:
                node.right = _insert(node.right)

            self.update_height(node)
            return self.balance_tree(node)
            
        self.root = _insert(self.root)

    def dequeue(self):
        if not self.root:
            return None
            
        current = self.root
        while current.left:
            current = current.left
        highest = (current.value, current.priority)
        
        def delete_left(node):
            if not node.left:
                return node.right 
                
            node.left = delete_left(node.left)
            self.update_height(node)
            return self.balance_tree(node)

        self.root = delete_left(self.root)
        return highest
    
    def view_queue(self):
        elements = []
        
        def _traverse(node):
            if node:
                _traverse(node.left)
                elements.append((node.value, node.priority))
                _traverse(node.right)
                
        _traverse(self.root)
        return elements
    
    def height(self, node):
        return node.height if node else 0

    def update_height(self, node):
        node.height = 1 + max(self.height(node.left), self.height(node.right))

    def balance_factor(self, node):
        return self.height(node.left) - self.height(node.right) if node else 0

    def rotate_right(self, unbalanced_node):
        new_root = unbalanced_node.left
        unbalanced_node.left = new_root.right
        new_root.right = unbalanced_node
        
        self.update_height(unbalanced_node)
        self.update_height(new_root)
        return new_root

    def rotate_left(self, unbalanced_node):
        new_root = unbalanced_node.right
        unbalanced_node.right = new_root.left
        new_root.left = unbalanced_node
        
        self.update_height(unbalanced_node)
        self.update_height(new_root)
        return new_root

    def balance_tree(self, node):
        balance = self.balance_factor(node)

        if balance > 1:
            if self.balance_factor(node.left) < 0:
                node.left = self.rotate_left(node.left)
            return self.rotate_right(node)

        if balance < -1:
            if self.balance_factor(node.right) > 0:
                node.right = self.rotate_right(node.right)
            return self.rotate_left(node)

        return node