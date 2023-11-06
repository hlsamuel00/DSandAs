class Node:
    def __init__(self, value):
        self.value = value
        self.next: 'Node' = None
        self.prev: 'Node' = None

    def __repr__(self) -> str:
        return f'Node(value: {self.value} | next: {self.next})'

class Deque:
    def __init__(self) -> None:
        self.head: Node = None
        self.tail: Node = None
        self._size: int = 0


    def is_empty(self) -> bool:
        return self._size == 0

    def size(self) -> int:
        return self._size

    def add_front(self, val) -> None:
        self._size += 1
        new_node = Node(val)

        if not self.head:
            self.head = self.tail = new_node

        new_node.next = self.head
        self.head.prev = new_node
        self.head = new_node
        

    def add_end(self, val) -> None:
        self._size += 1
        new_node = Node(val)

        if not self.tail:
            self.head = self.tail = new_node

        new_node.prev = self.tail
        self.tail.next = new_node
        self.tail = new_node

    def remove_front(self):
        self._size = max(0, self._size - 1)

        if self.head:
            old_head = self.head
            self.head = self.head.next
            old_head.next = None

            return old_head.value

        return


    def remove_end(self) -> Node:
        self._size = max(0, self._size - 1)

        if self.tail:
            old_tail = self.tail
            self.tail = self.tail.prev
            self.tail.next = None
            
            return old_tail.value
        
        return

    def as_list(self) -> list[Node]:
        lst, current = [self.head.value], self.head

        while current := current.next:
            lst.append(current.value)
        
        return lst
    

if __name__ == '__main__':
    dq = Deque()

    for i in range(1,6):
        dq.add_front(i)

    for i in range(6, 11):
        dq.add_end(i)

    print(dq.as_list())
    #Output: [5, 4, 3, 2, 1, 6, 7, 8, 9, 10]

    dq.remove_end()
    print(dq.as_list())
    # Output: [5, 4, 3, 2, 1, 6, 7, 8, 9]

    dq.remove_front()
    print(dq.as_list())
    # Output: [4, 3, 2, 1, 6, 7, 8, 9]