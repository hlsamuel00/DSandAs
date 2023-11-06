class Node:
    def __init__(self, val = None):
        self.val = val
        self.prev: 'Node' = None

class Stack:
    def __init__(self) -> None:
        self.head: Node = None
        self._size = 0

    def __repr__(self) -> str:
            if self.is_empty():
                return '[]'

            string = '[ '

            current = self.head

            for i in range(self._size):
                string += str(current.val)
                if i < self._size - 1:
                    string += ', '
                current = current.prev
            
            string += ' ]'
            return string

    def push(self, item):
        self._size += 1
        
        old_head = self.head
        self.head = Node(item)
        self.head.prev = old_head

    def pop(self):
        if self.is_empty():
            return
        
        self._size -= 1
        old_head = self.head
        self.head = self.head.prev
        return old_head.val 


    def is_empty(self):
        return self.size() == 0
    
    def peek(self):
        return self.head.val  

    def size(self):
        return self._size  
    
if __name__ == '__main__':
    
    stack = Stack()
    for i in range(5):
        stack.push(i)


    print(stack)

    for _ in range(6):
        print(stack.pop())