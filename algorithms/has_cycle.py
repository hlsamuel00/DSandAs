class Node:
    def __init__(self, val, next : 'Node' = None) -> None:
        self.val = val
        self.next = next

class LinkedList:
    def __init__(self, head: Node = None, size: int = 0) -> None:
        self.head = head
        self._size = size

    def __repr__(self) -> str:
        if not self._size:
            return '[ head -> None ]'
        
        string = '[ head -> '

        current = self.head
        for i in range(self._size):
            string += str(current.val)
            if i < self._size - 1:
                string += ' -> '
            current = current.next
        
        string += ' -> None ]'
        return string

    def insert_front(self, value) -> None:
        new_node = Node(value)
        self._size += 1

        if self.head:
            new_node.next = self.head
        
        self.head = new_node

    def insert_end(self, value) -> None:
        self._size += 1

        current = self.head
        while current.next:
            current = current.next
        
        current.next = Node(value)

    def remove_front(self):
        self._size = max(0, self._size - 1)

        if self.head:
            old_head = self.head
            self.head = self.head.next
            old_head.next = None

            return old_head.val
        
        return None
    
    def get_size(self):
        return self._size

#==============================================================================================================

def has_cycle(linked_list: LinkedList):
    slow = fast = linked_list.head

    while fast and fast.next:
        slow = slow.next
        fast == fast.next.next
        if fast == slow:
            return True
    
    return False