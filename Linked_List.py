class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Creating Nodes
node1 = Node(5)
node2 = Node(10)
node3 = Node(15)
node4 = Node(20)
node5 = Node(25)

# Connecting nodes
node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5

# Printing the Linked List
current = node1
print("Linked List : ")
while current is not None:
    print(current.data, end=" -> ")
    current = current.next
print("None")