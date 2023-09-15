def bubble_sort(input_data):
    for i in range(len(input_data)):
        swapped = False
        for j in range(0, len(input_data)-i-1):
            if input_data[j] > input_data[j+1]:
                input_data[j],input_data[j+1] = input_data[j+1],input_data[j]
                swapped = True
        if not swapped:
            break

input_data = [-2,45,0,11,-9]
print("Before sorting:", input_data)
bubble_sort(input_data)
print("After sorting:", input_data)