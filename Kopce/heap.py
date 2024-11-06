from abc import ABC


class Heap(ABC):
    def __init__(self, min=True, values=None):
        self.min = min
        self.values = []
        if values is not None:
            for value in values:
                self.insert(value)

    def get_parent(self, index):
        if index > self.n_children:
            return (index-1)//self.n_children
        else:
            return 0

    def get_children(self, index):
        return self.n_children*index, self.n_children*index + 1

    def _insert(self, value, parent_index, element_index):
        self.values[parent_index], self.values[element_index] = value, self.values[parent_index]
        element_index = parent_index
        parent_index = self.get_parent(element_index)

        return parent_index, element_index

    def insert(self, value: any):
        self.values.append(value)
        element_index = len(self.values) - 1
        parent_index = self.get_parent(element_index)

        if self.min:
            while element_index > 0 and self.values[parent_index] > value:
                parent_index, element_index = self._insert(value, parent_index, element_index)
        else:
            while element_index > 0 and self.values[parent_index] < value:
                parent_index, element_index = self._insert(value, parent_index, element_index)

    def pop(self) -> any:
        pass

    def display(self) -> None:
        pass


class BinaryHeap(Heap):
    def __init__(self, min=True, values=None):
        self.n_children = 2
        super().__init__(min, values)


class FiveArHeap(Heap):
    def __init__(self, min=True, values=None):
        self.n_children = 5
        super().__init__(min, values)


class SevenArHeap(Heap):
    def __init__(self, min=True, values=None):
        self.n_children = 7
        super().__init__(min, values)


if __name__ == '__main__':
    binary_heap = BinaryHeap(values=[4, 6, 1, 10, 3], min=False)
    binary_heap.insert(0)

    five_ar_heap = FiveArHeap(values=[4, 6, 1, 10, 3, 88, 10])
    five_ar_heap.insert(0)
    pass

    seven_ar_heap = SevenArHeap(values=[4, 6, 1, 10, 3, 88, 10, 11, 3, 2, 98, 0, 22, 4])
    seven_ar_heap.insert(0)
    pass
