class Node:
    def __init__(self, val) -> None:
        self.val = val
        self.next: 'Node'= None

class LinkedList:
    def __init__(self) -> None:
        self.head: Node = None
        self._size: int = 0

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
        self._size += 1
        
        old_head = self.head
        self.head = Node(value)
        self.head.next = old_head

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
        
        return 
    
    def get_size(self):
        return self._size


#==============================================================================================================
# TESTING
#==============================================================================================================

if __name__ == '__main__':
    linkedlist = LinkedList()
    
    for i in range(1, 6):
        linkedlist.insert_front(i)

    print(linkedlist)
    # Output: 5|4|3|2|1

    for i in range(6, 11):
        linkedlist.insert_end(i)

    print(linkedlist)
    # Output: 5|4|3|2|1|6|7|8|9|10

    linkedlist.remove_front()
    print(linkedlist)
    # Output: 4|3|2|1|6|7|8|9|10
    
