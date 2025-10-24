class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def hasCycle(head):
    slow = head
    fast = head
    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            print("Cycle detected in the linked list.")
            print("Meeting point data:", slow, fast)
            return True
    return False


head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)
head.next.next.next.next = head.next  # Creating a cycle for testing

hasCycle(head)

def func(arr):
    arr[0] += 1

a = [1,2,3,4,5]
func(a)
print(a)  # Output: [2, 2, 3, 4,

b = 5

def increment(x):
    x += 1
    
increment(b)
print(b)  # Output: 5

c = Node(10)

def modify_node(node):
    node.data += 5

modify_node(c)
print(c.data)  # Output: 15