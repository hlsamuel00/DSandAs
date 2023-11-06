class Node:
    def __init__(self, key, value) -> None:
        self.key = key
        self.value = value
        self.next: 'Node' = None
        self.prev: 'Node' = None

class Dequeue:
    def __init__(self):
        self.tail: Node = None
        self.head: Node = None

    def delete(self, node: Node):
        
        if node.prev:
            node.prev.next = node.next
        
        if node.next:
            node.next.prev = node.prev

        if node == self.head:
            self.head = node.next

        if node == self.tail:
            self.tail = node.prev

        node.prev = node.next = None
        return node
        

    def add_to_back(self, node: Node):
        if not self.tail:
            self.head = self.tail = node
            return

        node.prev = self.tail    
        self.tail.next = node
        self.tail = node

    def remove_from_front(self):
        old_head = self.head
        self.head = self.head.next
        old_head.next.prev = old_head.next = None
        return old_head.key
    
    def as_list(self) -> list:
        lst, current = [self.head.key], self.head

        while current := current.next:
            lst.append(current.key)

        return lst


class LRUCache:
    def __init__(self, capacity: int) -> None:
        self.queue = Dequeue()
        self.capacity = capacity
        self.size = 0
        self.in_cache = {}

    def __repr__(self) -> str:
        string = '['
        que_list = self.queue.as_list()

        for idx, key in enumerate(que_list):
            node = self.in_cache[key]
            string += f'({key},{node.value})'
            if idx < len(que_list) - 1:
                string += ', '

        string += ']'
        return string

    def set(self, key, val) -> None:
        if self.size < self.capacity or key in self.in_cache:
            self.size += (key not in self.in_cache)
            if key in self.in_cache:
                node = self.in_cache[key]
                self.queue.delete(node)

            self.in_cache[key] = Node(key,val)
            self.queue.add_to_back(self.in_cache[key])
            return
        
        popped_key = self.queue.remove_from_front()
        del self.in_cache[popped_key]
        new_node = Node(key, val)
        self.in_cache[key] = new_node
        self.queue.add_to_back(new_node)
        

    def get(self, key):
        if key in self.in_cache:
            node = self.in_cache[key]
            self.queue.delete(node)
            self.queue.add_to_back(node)
            return node.value
        
        return None


if __name__ == '__main__':
    cache = LRUCache(3)
    for i in range(1,7):
        cache.set(i, i)
        print(cache)

    print(cache.get(4))
    print(cache)
    print(cache.get(2))
    print(cache)
    print(cache.get(5))
    print(cache)
