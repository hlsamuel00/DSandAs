class Node:
    def __init__(self, val = None):
        self.val = val
        self.prev: 'Node' = None 
        self.next: 'Node' = None   

    def __repr__(self) -> str:
        return f'Node: {self.val}'

class DoublyLinkedList:
    def __init__(self) -> None:
        self.head: Node = None
        self.tail: Node = None
        self._size: int = 0

    def __repr__(self) -> str:
        if not self._size: 
            return '[ head -> None <- tail ]'


        string = '[ head -> '

        current = self.head
        for i in range(self._size):
            string += str(current.val)
            if i < self._size - 1:
                string += ' <==> '
            current = current.next
        
        string += ' <- tail ]'
        return string

    def prepend(self, item) -> None:
        new_node = Node(item)

        self._size += 1
        if not self.head:
            self.head = self.tail = new_node

        new_node.next = self.head
        self.head.prev = new_node
        self.head = new_node

    def insert_at(self, item, index: int):

        if index > self._size:
            raise ValueError
        elif index == self._size:
            self.append(item)
            return
        elif index == 0:
            self.prepend(item)
            return
        
        self._size += 1
        current = self.head
        for _ in range(index):
            current = current.next
        
        new_node = Node(item)
        new_node.next = current
        new_node.prev = current.prev
        current.prev = new_node
        current.prev.next = current

        

    def append(self, item):
        self._size += 1
        new_node = Node(item)
        if not self.tail:
            self.head = self.tail = new_node
        
        new_node.prev = self.tail
        self.tail.next = new_node
        self.tail = new_node

    def remove(self, item): 
        current = self.head
        
        for _ in range(self._size):
            if (current := current.next).val == item:
                break
        
        if not current:
            return None
        
        self._size -= 1
        if self._size == 0:
            self.head = self.tail = None
            return current.val 
        
        if current.prev:
            current.prev = current.next
        
        if current.next:
            current.next = current.prev

        if current == self.head:
            self.head = current.next

        if current == self.tail:
            self.tail = current.prev

        current.prev = current.next = None
        return current.val
    
    def size(self):
        return self._size
    
    def get(self, index: int):
        pass
        

    def remove_at(self, index: int):
        pass