

def buble_sort(to_sort_array: list):
    n = len(to_sort_array)
    for i in range(n):
        for j in range(1, n-i):
            element1, element2 = to_sort[j], to_sort[j-1]
            if element1 < element2:
                to_sort[j], to_sort[j-1] = element2, element1
    return to_sort_array


if __name__ == '__main__':
    to_sort = [5, 1, 10, 5]
    sorted_list = buble_sort(to_sort)
    print(sorted_list)
