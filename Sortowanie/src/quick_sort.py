def main():
    array = [2, 10, 1, 22, 33,11,76,0,0, 23,-1, 123,11, 304,2,40]
    print(quickSort(array))
    
    

def quickSort(array, left = None, right = None):
    if left is None and right is None:
        array = array.copy()
        left = 0
        right = len(array)-1

    if left < right: #in other case the array has len = 1 
        partitionPosition = part(array, left, right)  
        quickSort(array, left, partitionPosition -1) #sorting on the left of the chosen element
        quickSort(array, partitionPosition+1, right) #sorting on the right

    if left==0 and right ==len(array)-1: #only first iteration should return anythong
        return array    


def part(array, left, right):
    i = left        #iterating through the left array
    j = right - 1   #iterating through the right array
    pivotValue = array[right] #we just choose the last element as the value to compare

    while (i<j): 
        while (i < right and array[i] <pivotValue): #i 'looks' for an element bigger than/equal to our pivot
            i+=1 

        while( j > left and array[j] >= pivotValue): #j 'looks' for an element smaller than our pivot
            j -=1 #not j+=1!!
                
        if i<j:
                array[i], array[j] = array[j], array[i] #now we switch i <-> j
  

    if (array[i]>pivotValue): #switching i<->p
        array[i], array[right] = array[right], array[i]
    return i #we need it in our quickSort function

if __name__ =='__main__':
    main()