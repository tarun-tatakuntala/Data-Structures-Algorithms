"""Pekata. First card chinnadhi ani assume cheskuni migatha card sort cheskovadam"""
def insertion_sort(array):
    for i in range(1,len(array)):
        temp =  array[i]
        j = i-1
        while j > -1 and temp < array[j]:
            array[j+1] = array[j]
            array[j] = temp
            j -=1
    return array


print(insertion_sort([4,2,6,5,1,3]))