

def insertion_sort(to_sort: list):
    n = len(to_sort)
    for i in range(1, n):
        element = to_sort[i]
        j = i - 1
        while element < to_sort[j] and j>=0:
            to_sort[j], to_sort[j+1] = element, to_sort[j]
            j -= 1
    return to_sort


if __name__ == '__main__':
    to_sort = [4, 1, 8, 1, 2, 4]
    sorted_list = insertion_sort(to_sort)
    print(sorted_list)
    pass
