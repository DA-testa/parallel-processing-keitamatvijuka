# python3
# Keita Matvijuka 221RDB506 13. Grupa



def build_heap(data):
    swaps = []
    min_heap = MinHeap()
    min_heap.build_heap(data, swaps)
    return swaps
            
            class MinHeap:
    def __init__(self):
        self.heap = []

    def parent(self, i):
        return (i - 1) // 2

    def left_child(self, i):
        return 2 * i + 1

    def right_child(self, i):
        return 2 * i + 2

    def sift_down(self, i, swaps):
        min_index = i
        left = self.left_child(i)
        if left < len(self.heap) and self.heap[left] < self.heap[min_index]:
            min_index = left
        right = self.right_child(i)
        if right < len(self.heap) and self.heap[right] < self.heap[min_index]:
            min_index = right
        if i != min_index:
            swaps.append((i, min_index))
            self.heap[i], self.heap[min_index] = self.heap[min_index], self.heap[i]
            self.sift_down(min_index, swaps)

    def build_heap(self, data, swaps):
        self.heap = data[:]
        for i in range(len(data)//2, -1, -1):
            self.sift_down(i, swaps)

    def get_heap(self):
        return self.heap

def main():
    Input = input()
    if "I" in Input:
        n = int(input())
        data = list(map(int, input().split()))
        assert len(data) == n

    if "F" in Input:
        filepath = "tests/" + input()
        with open(filepath, 'r') as file:
            n = int(file.readline().strip())
            data = list(map(int, file.readline().strip().split()))
            assert len(data) == n

    swaps = build_heap(data)
    print(len(swaps))
    for i, j in swaps:
        print(i, j)


if __name__ == "__main__":
    main()

