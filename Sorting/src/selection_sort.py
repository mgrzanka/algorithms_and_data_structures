def main():
    array = [10, 20, 1, 2203, 1, 30, -1]
    print(selectionSort(array))
    

def selectionSort(arr):
    array = arr.copy()
    for i in range(0, len(array)-1):
        minValIndex = i #najpierw ten pierwszy element  jest najmniejszy
        for j in range(i +1, len(array)): #i-tego elementu nie musimy porównywać do samego siebie
            if(array[j] <array[minValIndex]):
                minValIndex = j
        #teraz minValIndex pokazuje na najmniejsza wartość w całej tablicy
        array[i], array[minValIndex] = array[minValIndex], array[i]
    return array


if __name__ == "__main__":
    main()