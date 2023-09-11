"""
Binary search can be performed mainly using 2 methods.
1. Iterative method
2. Recursive method(Divide & Conquer)

"""
def binary_search(array, target):
    low = 0
    high = len(array)-1

    while low<=high:
        mid = (low+high)//2         #Finding middle element i.e 4
        if (array[mid] == target):
            return mid
        elif array[mid] < target:   #array[4] < 3 i.e 40 < 3 false
            low = mid + 1
        else:
            high = mid - 1          #array[4] > 3 i.e 40 > 3 true
    return -1

array = [2,3,4,10,40]
target = 3
result = binary_search(array, target)

if result == -1:
    print("Element not found")
else:
    print("Element found at:",result)

