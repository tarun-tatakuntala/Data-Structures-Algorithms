def insertion_sort(array):
    for i in range(1,len(array)):
        temp =  array[i]
        j = i-1
        while temp < array[j] and j > -1:
            array[j+1] = array[j]
            array[j] = temp
            j -=1
    return array


print(insertion_sort([4,2,6,5,1,3]))