"""
Recursive method is nothing but divide and conquer approach. 
In recursive method, array is broken down until the target element is found.

"""
def binary_search(array, low, high, target):

    if low <= high:
        mid = (low + high)//2
        if array[mid] == target:
            return mid
        elif array[mid] > target:
            return binary_search(array, low, mid-1, target)
        else:
            return binary_search(array, mid+1, high, target)
    return -1

array = [2,3,4,10,40]
target = 3

result = binary_search(array, 0, len(array)-1, target)