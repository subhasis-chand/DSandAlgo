class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        temp = self.head
        while temp.next is not None:
            temp = temp.next
        temp.next = new_node
        new_node.prev = temp

    def display(self):
        temp = self.head
        while temp is not None:
            print(temp.data, end=" <-> ")
            temp = temp.next
        print("None")

dll = DoublyLinkedList()
dll.append(1)
dll.append(2)
dll.append(3)
dll.display()