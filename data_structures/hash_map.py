class Node:
    def __init__(self, key, value = None) -> None:
        self.key = key
        self.value = value
        self.next: 'Node' = None

    def __repr__(self) -> str:
        return f'Node: (key: {self.key} | value: {self.value} | next: {self.next})'

class HashMap:
    def __init__(self, capacity: int):
        self.map = [Node('temp') for _ in range(capacity)] 
        self.capacity = capacity

    def __repr__(self) -> str:
        string = ''
        for idx in range(self.capacity):
            string += f'{idx}: '
            current = self.map[idx]
            while current:
                string += f'{current.value} | '
                current = current.next
            string += '\n'

        return string

    def get(self, key):
        idx = self._hash_index(key)
        current = self.map[idx]

        while current:
            if current.key == key:
                return current.value
            current = current.next

    def put(self, key, val):
        idx = self._hash_index(key)
        current = self.map[idx]

        if current.key == 'temp' or current.key == key:
            current.key = key
            current.value = val
            return

        while current.next:
            current = current.next

        current.next = Node(key, val)

    def delete(self, key):
        idx = self._hash_index(key)
        prev = None
        current = self.map[idx]

        while current:
            if current.key == key:
                if not current.next:
                    current.key = 'temp'
                    current.value = None
                    return
                
                if not prev:
                    self.map[idx] = current.next
                    return

                prev.next = current.next
                return
            
            prev = current
            current = current.next

    def _hash_index(self, key) -> int:
        return key % self.capacity


if __name__ == '__main__':
    map = HashMap(3)
    for i in range(10):
        map.put(i, 2**i)

    print(map)
    # Output: 
    # 0: 1 |  8 |  64 | 512
    # 1: 2 | 16 | 128
    # 2: 4 | 32 | 256

    print(map.get(4))
    # Output: 16

    for i in range(3):
        map.delete(i)

    print(map)
    # Output: 
    # 0:  8 |  64 | 512
    # 1: 16 | 128
    # 2: 32 | 256

    print(map.get(9))
    # Output: 512

    print(map.get(11))
    # None