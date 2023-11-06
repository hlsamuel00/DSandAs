class Node:
    def __init__(self, val = None):
        self.val = val
        self.next: 'Node' = None

class Queue:
    def __init__(self) -> None:
        self.head: Node = None
        self.tail: Node = None
        self._size = 0

    def __repr__(self) -> str:

        if self.is_empty():
            return '[]'

        string = '[ head -> '

        current = self.head
        for i in range(self._size):
            string += str(current.val)
            if i < self._size - 1:
                string += ', '
            current = current.next
        
        string += ' <- tail ]'
        return string

    def enqueue(self, item):
        new_tail = Node(item)
        self._size += 1  
        
        if not self.tail:
            self.tail = self.head = new_tail
            return

        self.tail.next = new_tail
        self.tail = new_tail

    def deque(self):
        if self.is_empty():
            return None
        
        self._size -= 1
        head = self.head
        self.head = self.head.next
        head.next = None

        if self.is_empty():
            self.tail = self.head

        return head.val

    def peek(self):
        return self.head.val
    
    def is_empty(self):
        return self._size == 0
    
    def size(self):
        return self._size
    

if __name__ == '__main__':
    que = Queue()

    for i in range(10):
        que.enqueue(i)
    print(que)
    
    for i in range(11):
        print(que.deque())
        print(que)