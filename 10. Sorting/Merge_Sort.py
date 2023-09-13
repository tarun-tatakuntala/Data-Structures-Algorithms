def merge(list1,list2):
    combine = []
    i = j = 0
    while i < len(list1) and j < len(list2):
        if list1[i] < list2[j]:
            combine.append(list1[i])
            i+=1
        else:
            combine.append(list2[j])
            j+=1
    while i < len(list1):
            combine.append(list1[i])
            i+=1
    while j < len(list2):
            combine.append(list2[j])
            j+=1
    return combine

def merge_sort(array):
    if len(array) == 1:
        return array
    mid_index = int(len(array)/2)
    left = merge_sort(array[:mid_index])
    right = merge_sort(array[mid_index:])
    return merge(left, right)

array = [2,3,6,4,1,5]
print(array)
print(merge_sort(array))

