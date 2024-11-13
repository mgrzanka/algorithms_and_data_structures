from heap import BinaryHeap, FiveArHeap, SevenArHeap
from heapq import heapify, heappop

def test_empty_heap():
    binary = BinaryHeap(values=[])
    five = FiveArHeap(values=[])
    seven = SevenArHeap()

    #making sure that putting [] or None as our values doesn't cause an error & crash the program
    assert binary.values == []
    assert five.values == []
    assert seven.values == []


def test_all_equal_elements():
    binary = BinaryHeap(values=[1,1,1,1,1,1,1,1,1,1,1])
    five = FiveArHeap(values=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])
    seven = SevenArHeap(values=[-1])

    #should be the same length
    assert binary.values == [1,1,1,1,1,1,1,1,1,1,1]
    assert five.values == [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    assert seven.values == [-1]


def test_reverse_order():
    binary = BinaryHeap(values=[12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0])
    five = FiveArHeap(values=[12, 11, 10, 9, 8, 7, 6, 5, 4,3,2, 1, 0])
    seven = SevenArHeap(values=[12, 11, 10, 9, 8, 7, 6, 5, 4,3,2, 1, 0])
    maxBinary = BinaryHeap(values = [1, 2, 7, 3, 17, 19, 25, 36, 100], min=False) #testing a max heap as well

    assert binary.values == [0, 3, 1, 6, 4, 2, 8, 12, 9, 10, 5, 11, 7]
    assert five.values == [0, 3, 1, 10, 9, 8, 12, 7, 6, 5, 4, 11, 2]
    assert seven.values ==[0, 1, 11, 10, 9, 8, 7, 6, 12, 5, 4, 3, 2]
    assert maxBinary.values == [100, 36, 19, 25, 3, 2, 17, 1, 7]


def test_max_heap():
    binary = BinaryHeap(values=[21,17, 15, 14, 9, 13, 8, 5, 1], min=False)
    binary2 = BinaryHeap(values = [1, 2, 7, 3, 17, 19, 25, 36, 100], min=False)


    assert binary.values == [21,17, 15, 14, 9, 13, 8, 5, 1]
    assert binary2.values == [100, 36, 19, 25, 3, 2, 17, 1, 7]



def test_inserting_elements():
    binary = BinaryHeap(values=[21,17, 15, 14, 9, 13, 8, 5, 1], min=False)
    binary.insert(0) #should be last

    five = FiveArHeap(values=[], min=False)
    five.insert(0) #10 should go to the top but rest elements shouldn't change order
    five.insert(10)
    five.insert(9)
    five.insert(7)

    seven = SevenArHeap(values=[12, 11, 10, 9, 8, 7, 6, 5, 4,3,2, 1, 0])
    seven.insert(-77) #should go to the top and so, rearrange the heap


    #making sure that the values are correct after insert
    assert binary.values == [21, 17, 15, 14, 9, 13, 8, 5, 1, 0]
    assert five.values == [10, 0, 9, 7]
    assert seven.values == [-77, 0, 11, 10, 9, 8, 7, 6, 12, 5, 4, 3, 2, 1]


def test_poping_elements():
    list  =  [21,17, 15, 14, 9, 13, 8, 5, 1, 10, 22, 3, -1, 22, 32, 99, 0, 200]
    list2 = [12, 11, 10, 9, 8, 7, 6, 5, 4,3,2, 1, 0, -1, -2, -3, -4, -5, -6, -7, -8, -9, -10, -11, -12]
    list3 = [4, 6, 1, 10, 3, 88, 10, 11, 3, 2, 98, 99, 22, 4, 0, 8, 8, 8]

    binary = BinaryHeap(values=list)
    five = FiveArHeap(values=list2)
    seven = SevenArHeap(values=list3)

    heapify(list)
    heapify(list2)
    heapify(list3)

    #making sure pop() returns the correct element for all heaps
    assert binary.pop() == heappop(list)
    assert five.pop() == heappop(list2)
    assert seven.pop() == heappop(list3)



