class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

def serializePreOrder(node, arr):
    if node is None:
        arr.append(-1)
        return
    
    arr.append(node.data)
    serializePreOrder(node.left, arr)
    serializePreOrder(node.right, arr)

def serialize(root):
    arr = []
    serializePreOrder(root, arr)
    return arr

def deSerializeUtil(i, serialisedArr):
    if serialisedArr[i[0]] == -1:
        i[0] += 1
        return None

    node = Node(serialisedArr[i[0]])
    i[0] += 1
    node.left = deSerializeUtil(i, serialisedArr)
    node.right = deSerializeUtil(i, serialisedArr)
    return node

def deserialize(serialisedArr):
    i = [0]
    return deSerializeUtil(i, serialisedArr)

if __name__ == "__main__":
    root = Node(4)
    root.left = Node(3)
    root.left.left = Node(2)
    root.left.left.left = Node(1)

    root.right = Node(5)
    root.right.right = Node(6)
    root.right.right.right = Node(7)

    arr = []
    serializePreOrder(root, arr)
    print("Serialized Tree (Preorder):", arr)


