

def bubble_sort(to_sort: list):
    n = len(to_sort)
    sorted_list = to_sort.copy()
    for i in range(n):
        for j in range(1, n-i):
            element1, element2 = sorted_list[j], sorted_list[j-1]
            if element1 < element2:
                sorted_list[j], sorted_list[j-1] = element2, element1
    return sorted_list


if __name__ == '__main__':
    to_sort = [5, 1, 10, 5]
    sorted_list = bubble_sort(to_sort)
    print(sorted_list)
