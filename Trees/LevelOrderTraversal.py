class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

    #       5
    #     / \
    #   12   13
    #   /  \    \
    #  7    14   2
    # /  \ /  \  / \
    #17 23 27  3 8  11


def level_order_rec(node, level, res):
    if node is None:
        return
    
    if len(res) == level:
        res.append([])
    print(res)

    res[level].append(node.data)

    level_order_rec(node.left, level + 1, res)
    level_order_rec(node.right, level + 1, res)

def level_order(root):
    res = []
    level_order_rec(root, 0, res)
    return res

def level_order_iterative(root):
    if root is None:
        return []
    
    res = []
    q = []

    q.append(root)

    while q:
        level = len(q)
        current_level = []

        for _ in range(level):
            node = q.pop(0)
            current_level.append(node.data)

            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        
        res.append(current_level)
    
    return res
    

if __name__ == "__main__":
    root = Node(5)
    root.left = Node(12)
    root.right = Node(13)

    root.left.left = Node(7)
    root.left.right = Node(14)

    root.right.right = Node(2)

    root.left.left.left = Node(17)
    root.left.left.right = Node(23)

    root.left.right.left = Node(27)
    root.left.right.right = Node(3)

    root.right.right.left = Node(8)
    root.right.right.right = Node(11)

    result = level_order(root)
    print("Level Order Traversal:", result)


    a = [1,2,3,]
    print(len(a), a)

    b = [[1], [2,3], [4,5,6]]
    print(len(b), b)
    b.append([3])
    print(len(b), b)
    b[1].append(7)
    print(len(b), b)
    print(len(b[1]), b[1][2])

    iterative_result = level_order_iterative(root)
    print("Level Order Traversal (Iterative):", iterative_result)
    