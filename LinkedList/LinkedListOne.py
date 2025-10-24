class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def appendNode(head, data):
    new_node = Node(data)
    if head is None:
        return new_node
    temp = head
    while temp.next is not None:
        temp = temp.next
    temp.next = new_node
    return head

def insertAtBeginning(head, data):
    new_node = Node(data)
    new_node.next = head
    return new_node

def addNodeAfterAnElement(head, target_data, new_data):
    if head is None:
        return head
    temp = head
    while temp is not None:
        if temp.data == target_data:
            new_node = Node(new_data)
            new_node.next = temp.next
            temp.next = new_node
            return head
        temp = temp.next
    return head

def deleteFromEnd(head):
    if head is None:
        return None
    if head.next is None:
        return None
    temp = head
    while temp.next.next is not None:
        temp = temp.next
    temp.next = None
    return head

def deleteFromBeginning(head):
    if head is None:
        return None
    return head.next

def deleteNodeByValue(head, target_data):
    if head is None:
        return None
    if head.data == target_data:
        return head.next
    temp = head
    while temp.next is not None:
        if temp.next.data == target_data:
            temp.next = temp.next.next
            return head
        temp = temp.next
    return head


def displayList(head):
    temp = head
    while temp is not None:
        print(temp.data, end=" -> ")
        temp = temp.next
    print("None")

###############################

head = None # Empty list
head = insertAtBeginning(head, 3) # List: 3 -> None
head = appendNode(head, 5)        # List: 3 -> 5 ->
displayList(head)
print("head: ",head)
print("Node class: ", Node)