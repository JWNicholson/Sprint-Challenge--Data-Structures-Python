class Node:
    def __init__(self, value=None, next_node=None):
        self.value = value
        self.next_node = next_node

    def get_value(self):
        return self.value

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        self.next_node = new_next

class LinkedList:
    def __init__(self):
        self.head = None

    def add_to_head(self, value):
        node = Node(value)

        if self.head is not None:
            node.set_next(self.head)

        self.head = node

    def contains(self, value):
        if not self.head:
            return False

        current = self.head

        while current:
            if current.get_value() == value:
                return True

            current = current.get_next()

        return False

# Initialize pointers - previous and nade as None, current_node as self.head
# Iterate through the linked list
# set next incoming node as the current next node.The old current node is now the previous node
# previous node becomes the current_node and current_node becomes the next node
# head moves to the previous node - that means backwards (thats why its called reversal)

    def reverse_list(self, node, prev):
        pass
