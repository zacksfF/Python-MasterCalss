class Node:
    def __init__(self, data):
        self.data = data
        self.next_node = None

class LinkedList:
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head is None

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        current = self.head
        while current.next_node:
            current = current.next_node
        current.next_node = new_node

    def prepend(self, data):
        new_node = Node(data)
        new_node.next_node = self.head
        self.head = new_node

    def delete(self, data):
        if self.head is None:
            return
        if self.head.data == data:
            self.head = self.head.next_node
            return
        current = self.head
        while current.next_node:
            if current.next_node.data == data:
                current.next_node = current.next_node.next_node
                return
            current = current.next_node

    def display(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next_node
        print("None")

# Usage example
my_list = LinkedList()
my_list.append(1)
my_list.append(2)
my_list.append(3)
my_list.prepend(0)
my_list.display()  # Output: 0 -> 1 -> 2 -> 3 -> None
my_list.delete(2)
my_list.display()  # Output: 0 -> 1 -> 3 -> None
