class MaxPriorityQueue:
    def __init__(self) -> None:
        self.arr = [None]

    def __repr__(self) -> str:
        output = '['
        for idx in range(1, len(self.arr)):
            output += str(self.arr[idx])
            if idx < len(self.arr) - 1:
                output += ', '

        output += ']'
        return output

    def insert(self, key) -> None:
        self.arr.append(key)
        self._swim()

    def _swim(self):
        idx = len(self.arr) - 1
        while idx // 2 and self.arr[idx//2] < self.arr[idx]:
            self.arr[idx], self.arr[idx//2] = self.arr[idx//2], self.arr[idx]
            idx //= 2

    def get_max(self):
        if self.is_empty():
            return
        
        return self.arr[1]

    def del_max(self):
        if self.is_empty():
            return 
        
        self.arr[1], self.arr[len(self.arr)-1] = self.arr[len(self.arr)-1], self.arr[1]
        val = self.arr.pop()
        self._sink()
        return val
        
    def _sink(self):
        idx = 1
        while idx * 2 < len(self.arr):
            current = self.arr[idx]
            left = self.arr[idx * 2]
            right = float('-inf')
            if idx * 2 + 1 < len(self.arr):
                right = self.arr[idx * 2 + 1]

            if current >= left and current >= right:
                return
            
            if left > right:
                self.arr[idx], self.arr[idx*2] = self.arr[idx*2], self.arr[idx]
                idx *= 2
            else:
                self.arr[idx], self.arr[idx*2+1] = self.arr[idx*2+1], self.arr[idx]
                idx = idx * 2 + 1

    def is_empty(self) -> bool:
        return len(self.arr) == 1

    def size(self) -> int:
        return len(self.arr) - 1
    
class MinPriorityQueue:
    def __init__(self) -> None:
        self.arr = [None]

    def __repr__(self) -> str:
        output = '['
        for idx in range(1, len(self.arr)):
            output += str(self.arr[idx])
            if idx < len(self.arr) - 1:
                output += ', '

        output += ']'
        return output

    def insert(self, key) -> None:
        self.arr.append(key)
        self._swim()

    def _swim(self):
        idx = len(self.arr) - 1
        while idx // 2 and self.arr[idx//2] > self.arr[idx]:
            self.arr[idx], self.arr[idx//2] = self.arr[idx//2], self.arr[idx]
            idx //= 2

    def get_min(self):
        if self.is_empty():
            return
        
        return self.arr[1]

    def del_min(self):
        if self.is_empty():
            return 
        
        self.arr[1], self.arr[len(self.arr)-1] = self.arr[len(self.arr)-1], self.arr[1]
        val = self.arr.pop()
        self._sink()
        return val
        

    def _sink(self):
        idx = 1
        while idx * 2 < len(self.arr):
            current = self.arr[idx]
            left = self.arr[idx * 2]
            right = float('inf')
            if idx * 2 + 1 < len(self.arr):
                right = self.arr[idx * 2 + 1]

            if current <= left and current <= right:
                return
            
            if left < right:
                self.arr[idx], self.arr[idx*2] = self.arr[idx*2], self.arr[idx]
                idx *= 2
            else:
                self.arr[idx], self.arr[idx*2+1] = self.arr[idx*2+1], self.arr[idx]
                idx = idx * 2 + 1

    def is_empty(self) -> bool:
        return len(self.arr) == 1

    def size(self) -> int:
        return len(self.arr) - 1
    
def heapsort(arr: list) -> None:
    pq = MinPriorityQueue()
    for item in arr:
        pq.insert(item)
    
    idx = 0
    while not pq.is_empty():
        arr[idx] = pq.del_min()
        idx += 1

if __name__ == '__main__':
    from random import randint
    arr = [randint(-100, 100) for _ in range(15)]
    print(arr)
    heapsort(arr)
    print(arr)