class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

def inorder_traversal(node, arr):
    if node is None:
        return
    
    inorder_traversal(node.left, arr)
    arr.append(node.data)
    inorder_traversal(node.right, arr)

def insert_bst(root, key):
    if root is None:
        return Node(key)
    
    if key < root.data:
        root.left = insert_bst(root.left, key)
    else:
        root.right = insert_bst(root.right, key)
    
    return root

def search_rec(node, key):
    if node is None:
        return False
    
    if node.data == key:
        return True
    
    if key > node.data:
        return search_rec(node.right, key)
    
    return search_rec(node.left, key)

def search_ite(node, key):
    current = False

    while node is not None:
        if node.data == key:
            current = True
            break
        elif key > node.data:
            node = node.right
        else:
            node = node.left
    return current

def minValue(node):
    if root.left is None:
        return root.data
    return minValue(root.left)

def getInorderSuccessor(node):
    current = node.right
    while current is not None and current.left is not None:
        current = current.left
    return current

def deleteNode(node, target):
    if node is None:
        return node
    
    if target < node.data:
        node.left = deleteNode(node.left, target)
    elif target > node.data:
        node.right = deleteNode(node.right, target)
    else:
        #  1 or 0 child
        if node.left is None:
            return node.right
        elif node.right is None:
            return node.left
        
        temp = getInorderSuccessor(node)
        node.data = temp.data
        node.right = deleteNode(node.right, temp.data)
    
    return node

if __name__ == "__main__":
    root = Node(22)
    root.left = Node(12)
    root.right = Node(30)
    root.left.left = Node(8)
    root.left.right = Node(20)
    root.left.right.right = Node(21)
    root.right.right = Node(35)

    arr = []
    inorder_traversal(root, arr)
    print("Inorder Traversal:", arr)

    insert_bst(root, 15)
    arr = []
    inorder_traversal(root, arr)
    print("Inorder Traversal after insertion:", arr)

    search_ite_result = search_ite(root, 21)
    print("Search 21 (iterative):", search_ite_result)

    search_rec_result = search_rec(root, 21)
    print("Search 21 (recursive):", search_rec_result)

    # newroot = deleteNode(root, 12)

