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
        last_index = self.n_children*index + self.n_children
        max_index = len(self.values)-1
        upper_boud = self.n_children if last_index < max_index else (max_index-self.n_children*index) % self.n_children

        children = [self.n_children*index + bias for bias in range(1, upper_boud+1, 1)]

        return children

    def get_child(self, index):
        """Returns smaller/bigger out of two children"""
        children_indexes = self.get_children(index)

        if children_indexes:
            values = [self.values[index] for index in children_indexes]
            if self.min:
                return children_indexes[values.index(min(values))]
            else:
                return children_indexes[values.index(max(values))]

    def _go_up(self, value, parent_index, element_index):
        """Goes up with the value while inputing"""
        self.values[parent_index], self.values[element_index] = value, self.values[parent_index]
        element_index = parent_index
        parent_index = self.get_parent(element_index)

        return parent_index, element_index

    def _go_down(self, child_index, element_index):
        """Goes down with the element while popping"""
        self.values[child_index], self.values[element_index] = self.values[element_index], self.values[child_index]
        element_index = child_index
        child_index = self.get_child(element_index)

        return child_index, element_index

    def insert(self, value: any):
        self.values.append(value)
        element_index = len(self.values) - 1
        parent_index = self.get_parent(element_index)

        if self.min:
            while element_index > 0 and self.values[parent_index] > value:
                parent_index, element_index = self._go_up(value, parent_index, element_index)
        else:
            while element_index > 0 and self.values[parent_index] < value:
                parent_index, element_index = self._go_up(value, parent_index, element_index)

    def pop(self) -> any:
        to_pop = self.values[0]
        self.values[0] = self.values[-1]
        self.values.pop(-1)

        element_index = 0
        child_index = self.get_child(0)

        if self.min:
            while child_index is not None and self.values[element_index] > self.values[child_index]:
                child_index, element_index = self._go_down(child_index, element_index)
        else:
            while child_index is not None and self.values[element_index] < self.values[child_index]:
                child_index, element_index = self._go_down(child_index, element_index)

        return to_pop

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
    binary_heap = BinaryHeap(values=[4, 6, 1, 10, 3], min=True)
    binary_heap.insert(0)
    value = binary_heap.pop()

    five_ar_heap = FiveArHeap(values=[4, 6, 1, 10, 3, 88, 10])
    five_ar_heap.insert(0)
    value_5 = five_ar_heap.pop()
    pass

    seven_ar_heap = SevenArHeap(values=[4, 6, 1, 10, 3, 88, 10, 11, 3, 2, 98, 0, 22, 4])
    seven_ar_heap.insert(0)
    value_4 = seven_ar_heap.pop()
    pass
