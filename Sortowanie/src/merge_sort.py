

def merge_sort(to_sort: list):
    n = len(to_sort)
    if n <= 1:
        return to_sort

    split_point = n//2
    split1, split2 = merge_sort(to_sort[:split_point]), merge_sort(to_sort[split_point:])

    i = j = k = 0
    sorted_list = n * [None]
    while i < len(split1) and j < len(split2):
        if split1[i] < split2[j]:
            sorted_list[k] = split1[i]
            i += 1
        else:
            sorted_list[k] = split2[j]
            j += 1
        k += 1

    while i < len(split1):
        sorted_list[k] = split1[i]
        i += 1
        k += 1
    while j < len(split2):
        sorted_list[k] = split2[j]
        j += 1
        k += 1

    return sorted_list


if __name__ == '__main__':
    to_sort = [-9, 1, 5, 2, 9, 1, 0, -1, -2, 22]
    sorted_list = merge_sort(to_sort)
    print(sorted_list)
