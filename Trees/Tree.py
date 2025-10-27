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

def postorder_traversal(node):
    if node is None:
        return
    
    postorder_traversal(node.left)
    postorder_traversal(node.right)
    print(node.data, end=' ')
    

if __name__ == "__main__":
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.left = Node(6)

arr = []
inorder_traversal(root, arr)
print("Inorder Traversal:", arr)

