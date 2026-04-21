class MinHeap:
    def __init__(self):
        self.heap = []

    def push(self, item):
        self.heap.append(item)
        self._sift_up(len(self.heap) - 1)

    def pop(self):
        if not self.heap:
            raise IndexError("Спроба видалити елемент з порожньої купи")
        
        if len(self.heap) == 1:
            return self.heap.pop()
        
        root = self.heap[0]
        self.heap[0] = self.heap.pop()
        self._sift_down(0)
        
        return root

    def __bool__(self):
        return len(self.heap) > 0

    def _sift_up(self, idx):
        parent_idx = (idx - 1) // 2
        while idx > 0 and self.heap[idx] < self.heap[parent_idx]:
            self.heap[idx], self.heap[parent_idx] = self.heap[parent_idx], self.heap[idx]
            idx = parent_idx
            parent_idx = (idx - 1) // 2

    def _sift_down(self, idx):
        n = len(self.heap)
        while True:
            smallest = idx
            left_child = 2 * idx + 1
            right_child = 2 * idx + 2

            if left_child < n and self.heap[left_child] < self.heap[smallest]:
                smallest = left_child
            if right_child < n and self.heap[right_child] < self.heap[smallest]:
                smallest = right_child

            if smallest == idx:
                break
                
            self.heap[idx], self.heap[smallest] = self.heap[smallest], self.heap[idx]
            idx = smallest