
def insertion_sort(data, print_step=False):
    for i in range(len(data)):
        for j in range(0, i):
            if data[i]<data[j]:
                data.insert(j, data.pop(i))
                break
        if(print_step):
            print(data)

def selection_sort(data, print_step=False):
    for i in range(len(data)):
        min_index = i
        min_val = data[i]
        for j in range(i, len(data)):
            min_val = min(min_val, data[j])
            min_index = j if min_val == data[j] else min_index
        data[i], data[min_index] = data[min_index],data[i]
        if print_step:
            print(data)

def bubble_sort(data, print_step=False):
    is_sorted = False
    while not is_sorted:
        is_sorted = True
        for i in range(1, len(data)):
            if data[i-1]>data[i]:
                data[i-1], data[i] = data[i], data[i-1]
                is_sorted = False
        if print_step:
            print(data)

