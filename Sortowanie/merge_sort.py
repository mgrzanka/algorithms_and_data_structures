

def merge_sort(to_sort: list):
    n = len(to_sort)
    if n == 1:
        return to_sort

    split_point = int(n/2)
    split1, split2 = merge_sort(to_sort[:split_point]), merge_sort(to_sort[split_point:])

    i = j = 0
    n_split1, n_split2 = len(split1), len(split2)
    sorted_list = []
    while i < n_split1 and j < n_split2:
        if split1[i] < split2[j]:
            sorted_list.append(split1[i])
            i += 1
        else:
            sorted_list.append(split2[j])
            j += 1
    sorted_list.extend(split1[i:]) if j == n_split2 else sorted_list.extend(split2[j:])
    return sorted_list


if __name__ == '__main__':
    to_sort = [-9, 1, 5, 2, 9, 1, 0, -1, -2, 22]
    sorted_list = merge_sort(to_sort)
    print(sorted_list)
    pass
