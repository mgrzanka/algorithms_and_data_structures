

def insertion_sort(to_sort: list):
    n = len(to_sort)
    sorted_list = to_sort.copy()
    for i in range(1, n):
        element = sorted_list[i]
        j = i - 1
        while element < sorted_list[j] and j>=0:
            sorted_list[j+1] = sorted_list[j]
            j -= 1
        sorted_list[j + 1] = element
    return sorted_list


if __name__ == '__main__':
    to_sort = [1, 7, 4, 0, -1]
    sorted_list = insertion_sort(to_sort)
    print(sorted_list)
