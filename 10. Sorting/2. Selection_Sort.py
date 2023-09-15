def selection_sort(array, length):
    for i in range(length):
        min_index = i
        for j in range(i+1, length):
            if array[j] < array[min_index]:
                min_index = j
        array[i],array[min_index] = array[min_index], array[i]


array = [-2,45,0,11,-9,88,-97,-202,747]
length = len(array)
selection_sort(array, length)
print(array)