from doubly_linked_list import DoublyLinkedList


class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = None
        self.storage = DoublyLinkedList()

    def append(self, item):
        if self.current == None:
            self.current = 0
        
        if len(self.storage) < self.capacity:
            self.storage.add_to_tail(item)
            self.current += 1
        else:
            # Calculate the index to update
            self.current = self.current % self.capacity
            # Loop through the DLL until you find that index
            current_node = self.storage.head
            for _ in range(self.current):
                current_node = current_node.next
            current_node.value = item
            self.current += 1 

    def get(self):
        # Note:  This is the only [] allowed
        list_buffer_contents = []

        current_node = self.storage.head

        while current_node:
            list_buffer_contents.append(current_node.value)
            current_node = current_node.next

        return list_buffer_contents

# ----------------Stretch Goal-------------------


class ArrayRingBuffer:
    def __init__(self, capacity):
        pass

    def append(self, item):
        pass

    def get(self):
        pass