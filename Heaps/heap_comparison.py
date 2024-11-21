import gc
import os
import time
from random import randrange
import matplotlib.pyplot as plt
from Heaps.src.heap import BinaryHeap, FiveArHeap, SevenArHeap

#Wygeneruj wejściową listę liczb (np. 100000 losowych liczb z zakresu od 1 do
#300000), która posłuży dalej do badania wydajności.
heaps = {
        "binary": BinaryHeap,
        "five-ar": FiveArHeap,
        "seven-ar": SevenArHeap
    }

def generateList(num):
    '''Method returning a list of num elements with ints from range 1 to 300000'''
    list = [] * num
    for i in range(num):
        list.append(randrange(1, 300000))
    return list

def creationMeasurement(chosenHeap:str, list):
    gc_old = gc.isenabled()
    gc.disable()

    start = time.process_time()
    #creating the heap with an n-element list
    heap = heaps[chosenHeap](values = list, min=True)

    stop = time.process_time()

    if gc_old: gc.enable()

    return stop - start

def popMeasurement(heap, num:int):
    gc_old = gc.isenabled()
    gc.disable()

    start = time.process_time()
    #using the pop method n times
    for n in range(num):
        heap.pop()

    stop = time.process_time()

    if gc_old: gc.enable()

    return stop - start


#Dla każdego z kopców:
#sprawdź, czy heaps wstawiania i usuwania działają poprawnie, -- tests.py
#zmierz czas tworzenia kopca na podstawie n pierwszych liczb listy wejściowej (np. n = 10000, 20000, ..., 100000),
def creationTimeComparison()->None:
    numbers = list(range(10000, 100001, 10000))
    generated = generateList(100000)
    binTime = [] * len(numbers)
    fivTime = [] * len(numbers)
    sevTime = [] * len(numbers)

    print("\nMeasuring the time it takes to create a heap with n elements...")

    #for each n we add our results to lists for binary, five and seven
    for n in numbers:
        testingList = generated[:n]
        binTime.append(creationMeasurement("binary", testingList))
        fivTime.append(creationMeasurement("five-ar", testingList))
        sevTime.append(creationMeasurement("seven-ar", testingList))
        print(f"\t - n = {n} done")

    #adding to our plot
    plt.plot(numbers, binTime, label = "binary")
    plt.plot(numbers, fivTime, label = "five-ary")
    plt.plot(numbers, sevTime, label = "seven-ary")

    plt.title("Creation time of different heaps")
    plt.ylabel('time [seconds]')
    plt.xlabel('number of elements')
    plt.grid()
    plt.legend()
    plt.savefig(os.path.join("Kopce/plots","creation_time_comparison.png"))
    plt.show()

#zmierz czas wykonania n operacji usunięcia szczytu kopca (np. n = 10000,
#20000, ..., 100000) w kopcu, który dla każdego n został utworzony na podstawie całej listy wejściowej.
def popTimeComparison()->None:
    numbers = list(range(10000, 100001, 10000))
    generated = generateList(100000)
    print("\nMeasuring the time it takes to pop n elements...")

    binTime = [] * len(numbers)
    fivTime = [] * len(numbers)
    sevTime = [] * len(numbers)

    for n in numbers:
        #creating the heaps time&time again, so that for each measurement thay are exactly the same (unmodified by .pop())
        binary = BinaryHeap(min=True, values=generated)
        five = FiveArHeap(min=True, values=generated)
        seven = SevenArHeap(min=True, values=generated)

        #measure time that it takes to pop n elements
        binTime.append(popMeasurement(binary, n))
        fivTime.append(popMeasurement(five, n))
        sevTime.append(popMeasurement(seven, n))
        print(f"\t - n = {n} finished")

    #adding our results to the plot
    plt.plot(numbers, binTime, label = "binary")
    plt.plot(numbers, fivTime, label = "five-ary")
    plt.plot(numbers, sevTime, label = "seven-ary")

    plt.title("Time it takes to pop n elements:")
    plt.ylabel('time [seconds]')
    plt.xlabel('number of elements')
    plt.grid()
    plt.legend()
    plt.savefig(os.path.join("Kopce", "plots", "pop_time_comparison.png"))
    plt.show()



if __name__ == "__main__":
    creationTimeComparison()
    popTimeComparison()