class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
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

    def display(self):
        temp = self.head
        while temp is not None:
            print(temp, end=" -> ")
            temp = temp.next
        print("None")

l1 = LinkedList()
l1.append(1)
l1.append(2)
l1.append(3)
l1.display()