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

def preorder_traversal(node):
    if node is None:
        return
    
    print(node.data, end=' ')
    preorder_traversal(node.left)
    preorder_traversal(node.right)

def buildBalancedTree(arr, left, right):
    if left > right:
        return None
    
    mid = (left + right) // 2
    node = Node(arr[mid])

    node.left = buildBalancedTree(arr, left, mid - 1)
    node.right = buildBalancedTree(arr, mid + 1, right)

    return node

def balancedbst(root):
    inorderarr = []
    inorder_traversal(root, inorderarr)

    return buildBalancedTree(inorderarr, 0, len(inorderarr) - 1)

if __name__ == "__main__":
    root = Node(4)
    root.left = Node(3)
    root.left.left = Node(2)
    root.left.left.left = Node(1)

    root.right = Node(5)
    root.right.right = Node(6)
    root.right.right.right = Node(7)

    arr = []
    # inorder_traversal(root, arr)
    # print("Inorder Traversal:", arr)

    preorder_traversal(root)

    balanced_root = balancedbst(root)
    # balanced_arr = []
    # inorder_traversal(balanced_root, balanced_arr)
    # print("Inorder Traversal of Balanced BST:", balanced_arr)

    print("Preorder Traversal of Balanced BST:", end=' ')
    preorder_traversal(balanced_root)



