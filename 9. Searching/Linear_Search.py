"""Linear search is an basic search algorithm. In this algorithm, we traverse through the list until the search element is found."""

def linear_search(array,n,x):
    for i in range(0, n):
        if (array[i] == x):
            return i
    return -1

array = [2,4,0,1,3]
x = 1
n = len(array)
result = linear_search(array,n,x)
if (result == -1):
    print("Element not found")
else:
    print("Element found at: ", result)