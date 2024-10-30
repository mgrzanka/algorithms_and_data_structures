import os
import time
import gc
import matplotlib.pyplot as plt
from src.buble_sort import bubble_sort
from src.insertion_sort import insertion_sort
from src.selection_sort import selectionSort
from src.merge_sort import merge_sort
from src.quick_sort import quickSort
# sys.setrecursionlimit(limit)


def get_words(file_name: str, n: int):
    words = []
    with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), file_name)) as file:
        for line in file:
            words.extend(line.split())
            if len(words) >= n:
                break
    return words


def make_messure(words, algorithm_name: str):
    testing_map = {
        'bubble': bubble_sort, 'insert': insertion_sort, 'select': selectionSort, 'merge': merge_sort, 'quick': quickSort
    }
    gc_old = gc.isenabled()
    gc.disable()

    start = time.process_time()
    sorted_list = testing_map[algorithm_name](words)
    stop = time.process_time()

    if gc_old:
        gc.enable()

    return stop - start


def test():
    n_values = list(range(1000, 10001, 1000))
    algorithm_name = 'insert'
    times = []
    for indx, n in enumerate(n_values):
        words = get_words("pan-tadeusz.txt", n)
        times.append(make_messure(words, algorithm_name))
        print(f"{indx+1}/{len(n_values)} messures made")

    plt.plot(n_values, times)
    plt.title(f"{algorithm_name.upper()}: execution time dependent on the size of the problem")
    plt.xlabel('size of the problem')
    plt.ylabel('execution time')
    plt.grid()
    plt.savefig(f"{algorithm_name}_sort_plot.png")
    plt.show()


if __name__ == '__main__':
    test()
