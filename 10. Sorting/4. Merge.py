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


print(merge([1,2,7,8],[3,4,5,6]))