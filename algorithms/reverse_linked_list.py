class Node:
    def __init__(self, val, next : 'Node' = None, prev: 'Node' = None) -> None:
        self.val = val
        self.next = next
        self.prev = prev

    def __repr__(self) -> str:
        return f'Node: {self.val}'

class LinkedList:
    def __init__(self, head: Node = None, length: int = 0) -> None:
        self.head = head
        self._length = length

    def __repr__(self) -> str:
        string = '[ head -> '

        current = self.head
        for i in range(self._length):
            string += str(current.val)
            if i < self._length - 1:
                string += ' -> '
            current = current.next
        
        string += ' -> None ]'
        return string

    def insert_front(self, value) -> None:
        new_node = Node(value)
        self._length += 1

        if self.head:
            new_node.next = self.head
        
        self.head = new_node

    def insert_end(self, value) -> None:
        new_node = Node(value)
        self._length += 1

        if not self.head:
            self.head = new_node
            return

        current = self.head
        while current.next:
            current = current.next
        
        current.next = new_node

    def remove_front(self):
        self._length = max(0, self._length - 1)

        if self.head:
            old_head = self.head
            self.head = self.head.next
            old_head.next = None

            return old_head.val
        
        return None
    
    def get_length(self):
        return self._length
    

    
#==============================================================================================================

def reverse_linked_list(linked_list: LinkedList) -> None:
    current = linked_list.head
    prev = None

    while current:
        next = current.next
        current.next = prev
        prev = current
        current = next


    linked_list.head = prev

#============================================================================================================
# Testing
#============================================================================================================

if __name__ == '__main__':
    linkedlist = LinkedList()

    for i in range(1, 11):
        linkedlist.insert_front(i)

    print(linkedlist)

    for i in range(11, 16):
        linkedlist.insert_end(i)
    
    print(linkedlist)

    reverse_linked_list(linkedlist)
    print(linkedlist)
    
    reverse_linked_list(linkedlist)
    print(linkedlist)
    
    linkedlist.remove_front()
    print(linkedlist)
    print(linkedlist.head)
