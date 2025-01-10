import random

def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

def quick_sort_iterative(arr):
    stack = []
    stack.append(0)
    stack.append(len(arr) - 1)

    while stack:
        high = stack.pop()
        low = stack.pop()

        pivot_index = partition(arr, low, high)

        if pivot_index - 1 > low:
            stack.append(low)
            stack.append(pivot_index - 1)

        if pivot_index + 1 < high:
            stack.append(pivot_index + 1)
            stack.append(high)

array = random.sample(range(1,500), 70)
n = len(array)
print("Orignal Array:", array)
quick_sort_iterative(array)
print ("Sorted Array :", array)
