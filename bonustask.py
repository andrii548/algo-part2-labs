from lab3 import BinaryTree 

def deserialize_tree(filename):
    try:
        with open(filename, 'r') as file:
            data = file.read().strip()
    except FileNotFoundError:
        return None
    if not data:
        return None

    raw_values = data.split()
    values = [int(val) if val.lower() != 'null' else None for val in raw_values]

    if not values:
        return None

    root = BinaryTree(values[0])
    queue = [root]
    i = 1

    while queue and i < len(values):
        current = queue.pop(0)

        if i < len(values) and values[i] is not None:
            current.left = BinaryTree(values[i], parent=current)
            queue.append(current.left)
        i += 1

        if i < len(values) and values[i] is not None:
            current.right = BinaryTree(values[i], parent=current)
            queue.append(current.right)
        i += 1

    return root

def print_inorder(root):
    if not root:
        return
        
    
    first_node = root
    while first_node.left:
        first_node = first_node.left
        
    inorder_sequence = []
    current_node = first_node
    
    while current_node:
        inorder_sequence.append(str(current_node.value))
        current_node = BinaryTree.find_successor(current_node)
        
    print("INORDER ОБХІД:  " + " -> ".join(inorder_sequence))

def build_tree_lines(node):
    if node is None:
        return [], 0, 0, 0
    
    if node.right is None and node.left is None:
        line = str(node.value)
        width = len(line)
        return [line], width, 1, width // 2
        
    virt_left = node.right
    virt_right = node.left

    if virt_right is None:
        lines, n, p, x = build_tree_lines(virt_left)
        s = str(node.value)
        u = len(s)
        first_line = (x + 1) * ' ' + s + (n - x - 1) * ' '
        second_line = x * ' ' + '/' + (n - x - 1 + u) * ' '
        shifted_lines = [line + u * ' ' for line in lines]
        return [first_line, second_line] + shifted_lines, n + u, p + 2, x + 1 + u // 2
        
    if virt_left is None:
        lines, n, p, x = build_tree_lines(virt_right)
        s = str(node.value)
        u = len(s)
        first_line = x * ' ' + s + (n - x) * ' '
        second_line = (x + u) * ' ' + '\\' + (n - x - 1) * ' '
        shifted_lines = [u * ' ' + line for line in lines]
        return [first_line, second_line] + shifted_lines, n + u, p + 2, x + u // 2
        
    left, n, p, x = build_tree_lines(virt_left)
    right, m, q, y = build_tree_lines(virt_right)
    s = str(node.value)
    u = len(s)
    first_line = (x + 1) * ' ' + (n - x - 1) * ' ' + s + y * ' ' + (m - y) * ' '
    second_line = x * ' ' + '/' + (n - x - 1 + u + y) * ' ' + '\\' + (m - y - 1) * ' '
    
    if p < q:
        left += [n * ' '] * (q - p)
    elif q < p:
        right += [m * ' '] * (p - q)
        
    zipped_lines = zip(left, right)
    lines = [first_line, second_line] + [a + u * ' ' + b for a, b in zipped_lines]
    return lines, n + m + u, max(p, q) + 2, n + u // 2

def print_tree(root):
    if not root:
        return
        
    lines, *_ = build_tree_lines(root)
    
    for line in reversed(lines):
        swapped_line = line.replace('/', 'TEMP').replace('\\', '/').replace('TEMP', '\\')
        print(swapped_line)
    print("\n")

if __name__ == "__main__":
    test_filename = "inordertree.txt"
    tree_root = deserialize_tree(test_filename)
    
    if tree_root:
        print_inorder(tree_root)
        print_tree(tree_root)