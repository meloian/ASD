class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key
        self.count = 1

def insert(node, key):
    if node is None:
        return Node(key)
    else:
        if key == node.val:
            node.count += 1
        elif key < node.val:
            node.left = insert(node.left, key)
        else:
            node.right = insert(node.right, key)
    return node

def delete(node, key):
    if node is None:
        return node
    else:
        if key < node.val:
            node.left = delete(node.left, key)
        elif key > node.val:
            node.right = delete(node.right, key)
        else:
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left
            else:
                temp = min_node(node.right)
                node.val = temp.val
                node.right = delete(node.right, temp.val)
    return node

def min_node(node):
    current = node
    while current.left is not None:
        current = current.left
    return current

def print_tree(node, indent="", pos="root", last=True):
    if node is not None:
        if last:
            line_prefix = indent + "└── "
            indent_next = indent + "    "
        else:
            line_prefix = indent + "├── "
            indent_next = indent + "|   "

        print(f"{line_prefix}{node.val}({node.count})")
        print_tree(node.left, indent_next, 'left', node.right is None)
        print_tree(node.right, indent_next, 'right', True)

def count_and_build(prefix, node):
    subtree = None
    count = 0

    def traverse(n):
        nonlocal subtree, count
        if n is not None:
            if n.val.lower().startswith(prefix.lower()):
                count += n.count
                subtree = insert(subtree, n.val)
            traverse(n.left)
            traverse(n.right)
    traverse(node)
    return count, subtree

def remove_prefix(node, prefix):
    def traverse(n):
        if n is not None:
            n.left = traverse(n.left)
            n.right = traverse(n.right)
            if n.val.lower().startswith(prefix.lower()):
                return delete(n, n.val)
        return n
    return traverse(node)

def build_bst(file_path):
    root = None
    with open(file_path, 'r') as file:
        lines = file.readlines()
        for line in lines:
            words = line.split()
            for word in words:
                root = insert(root, word)
    return root

file_path = 'C:\\Users\\RocK4\\Desktop\\kpi\\ASD\\lab_5\\textfile.txt'
root = build_bst(file_path)
print("Main BST Structure:")
print_tree(root)

prefix = 'L'
count, subtree = count_and_build(prefix, root)
print(f"\nNumber of nodes starting with '{prefix}': {count}")
if count > 0:
    print(f"BST of words starting with '{prefix}':")
    print_tree(subtree)

root = remove_prefix(root, prefix)
print(f"\nMain BST after removing words starting with '{prefix}':")
print_tree(root) 