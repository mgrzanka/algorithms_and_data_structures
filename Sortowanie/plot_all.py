from tests import get_words, make_messure
import matplotlib.pyplot as plt
from src.buble_sort import bubble_sort
from src.insertion_sort import insertion_sort
from src.selection_sort import selectionSort
from src.merge_sort import merge_sort
from src.quick_sort import quickSort

#had to recreate this in order to use make_messure()
testing_map = {
        'bubble': bubble_sort, 
        'insert': insertion_sort, 
        'select': selectionSort, 
        'merge': merge_sort, 
        'quick': quickSort
}

def plotAllAlgorithms():
    charactersToSort = list(range(1000, 10001, 500))
    repetitionNumber = 10 #measurements can be made several times in order to make them more accurate
    timeValues = [] * len(charactersToSort)

    for algorithm in testing_map:
        print("Plotting algorithm: {}".format(algorithm), end=" ")
        timeValues = []
        for number in charactersToSort:
            words = get_words("pan-tadeusz.txt", number)
            timeMeasured = 0
            for i in range(0, repetitionNumber):
                timeMeasured += make_messure(words, algorithm)
            print(".", end =" ") #one dot for every repetition
            timeValues.append(timeMeasured/repetitionNumber) #average value
            
        
        print("\nAdding results of {} to the plot".format(algorithm))
        plt.plot(charactersToSort, timeValues, label = algorithm)

    #Creating the plot
    plt.title("Execution time dependent on the number of elements sorted:")
    plt.ylabel('time [seconds]')
    plt.xlabel('number of elements')
    plt.grid()
    plt.savefig(f"plot_of_all_alogithms.png")
    plt.legend()
    plt.show()

if __name__ =="__main__":
    plotAllAlgorithms()